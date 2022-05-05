from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Question(models.Model):
    """Модель вопросов"""
    question_id = models.PositiveIntegerField(unique=True, verbose_name='ид вопроса')
    question_text = models.TextField(verbose_name='текст вопроса')
    question_answer = models.TextField(verbose_name='ответ на вопрос')
    created_at = models.DateTimeField(verbose_name='время создания')
    value = models.PositiveIntegerField(verbose_name='очки', **NULLABLE)
    category = models.CharField(max_length=128, verbose_name='категория', **NULLABLE)

    def __str__(self):
        return f'Question: {self.question_text}'

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
        ordering = ['-id']