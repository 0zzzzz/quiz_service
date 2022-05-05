from django.http.response import HttpResponse, Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from quizapp.models import Question
from quizapp.serializers import QuestionSerializer
from quizapp.service import db_questions_add


class QuestionGet(APIView):
    def get(self, request):
        """Получение списка всех запросов из базы"""
        question = Question.objects.all()
        serializer = QuestionSerializer(question, many=True)
        return Response(serializer.data)

    def post(self, request):
        """Получение новых вопросов"""
        if Question.objects.filter().last():
            previous_question = Question.objects.filter().last()
            previous_question = previous_question.question_text
        else:
            previous_question = None
        if 'questions_num' in request.data:
            questions_num = request.data['questions_num']
            db_questions_add(questions_num)
        return HttpResponse(previous_question)


class QuestionUpdateAPIView(APIView):
    """Изменение вопроса"""

    @staticmethod
    def get_object(pk: int):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question)
        return Response(serializer.data)

    def put(self, request, pk):
        question = self.get_object(pk)
        serializer = QuestionSerializer(question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        question = self.get_object(pk)
        question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
