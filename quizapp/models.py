from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
# Во фласке сделать question_id == id (в диджанго автоматически выставляется)
class Question(models.Model):
    question_id = models.CharField(max_length=128, unique=True, verbose_name='ид вопроса')
    question_text = models.TextField(verbose_name='текст вопроса')
    question_answer = models.TextField(verbose_name='ответ на вопрос')
    created_at = models.DateTimeField(verbose_name='время создания')
