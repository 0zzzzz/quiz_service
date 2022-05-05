from django.urls import path
from quizapp import views as api

app_name = 'quizapp'

urlpatterns = [
    path('question_get/', api.QuestionGet.as_view(), name='question_get'),
    path('question_update/<int:pk>/', api.QuestionUpdateAPIView.as_view(), name='question_update'),
]
