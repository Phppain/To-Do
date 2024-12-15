from django.contrib import admin
from django.urls import path
from app.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainToDo, name='mainToDo'), # Переносит на главную страницу
    path('create/', createToDo, name='createToDo'), # В зависимости от типа запроса переносит на страницу создания to-do или сохраняет to-do в БД
    path(r'^delete/(?P<todo_id>\d+)/$', deleteToDo, name='deleteToDo'), # Удаляет to-do по id
    path(r'^edit/(?P<todo_id>\d+)/$', editToDo, name='editToDo') # Позволяет изменить to-do по id
]
