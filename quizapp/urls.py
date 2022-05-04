# from django.conf import settings
# from django.conf.urls.static import static
from django.urls import path
from quizapp import views as api

app_name = 'quizapp'

urlpatterns = [
    path('question_get/', api.QuestionGet.as_view(), name='question_get'),
]
