import datetime
import requests

from django.conf import settings
from quizapp.models import Question


def db_questions_add(questions_num):
    """добавляет новые вопросы из удаленного сервиса"""
    url = f'{settings.QUESTIONS_SERVICE}{questions_num}'
    url_answer = requests.get(url)
    response_data = url_answer.json()
    same_questions = 0
    for i in range(len(response_data)):
        if Question.objects.filter(question_id=response_data[i]['id']).exists():
            same_questions += 1
            print(same_questions)
        else:
            new_question = Question.objects.create(
                question_id=response_data[i]['id'],
                question_text=response_data[i]['question'],
                question_answer=response_data[i]['answer'],
                created_at=datetime.datetime.now()
            )
            new_question.save()
        if i == len(response_data) - 1 and same_questions > 0:
            return db_questions_add(same_questions)
