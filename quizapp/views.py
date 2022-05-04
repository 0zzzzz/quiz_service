# from django.shortcuts import render
# import datetime
# from django.http import Http404, HttpResponse
# from rest_framework import status
# from rest_framework.response import Response
import datetime

from django.http.response import HttpResponse, JsonResponse
from rest_framework.response import Response
from rest_framework.views import APIView

# from quizapp.models import Item
# from quizapp.serializers import ItemSerializer
# from quizapp.services.pdf_service import create_pdf
# import qrcode

# Create your views here.
from quizapp.models import Question
from quizapp.serializers import QuestionSerializer
import requests

from quizapp.service import db_questions_add


class QuestionGet(APIView):

    def get(self, request):
        item = Question.objects.all()
        serializer = QuestionSerializer(item, many=True)
        return Response(serializer.data)

    def post(self, request):
        response_data = None
        if Question.objects.filter().last():
            previous_question = Question.objects.filter().last()
        else:
            previous_question = None
        if 'questions_num' in request.data:
            questions_num = request.data['questions_num']
            response_data = db_questions_add(questions_num)
        return HttpResponse(previous_question)

