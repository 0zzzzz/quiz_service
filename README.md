# quiz_service

Запуск через docker-compose:
sudo docker-compose build
sudo docker-compose run web python manage.py migrate 
sudo docker-compose up
sudo docker-compose down


Эндпоинты:
http://{localhost}:8080/api/question_update/{int}/
	GET получить вопрос по ид
	PUT изменить вопрос
	DELETE удалить вопрос

http://{localhost}:8080/api/question_get/
	GET вывести все вопросы из базы
	POST записать в базу {int} случайных вопросов
		{
		    "questions_num": {int}
		}
