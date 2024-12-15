from django.contrib import admin
from django.urls import path
from app.views import createToDo, mainToDo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', mainToDo, name='mainToDo'), # Переносит на главную страницу
    path('create/', createToDo, name='createToDo') # В зависимости от типа запроса переносит на страницу создания to-do или сохраняет to-do в БД
]
