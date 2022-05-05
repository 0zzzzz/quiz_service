# quiz_service

sudo docker-compose build
sudo docker-compose up
docker-compose run web python manage.py migrate 
sudo docker-compose down

http://{localhost}:8080/api/question_update/{int}/
GET получить вопрос по ид
PUT изменить вопрос
DELETE удалить вопрос



http://0.0.0.0:8080/api/question_get/

Получить 10 случайных вопросов
{
    "questions_num": 10
}
