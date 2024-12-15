from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ToDo

def createToDo(request):
    if request.method == "POST":
        topic = request.POST['topic']
        description = request.POST['description']
        ToDo.objects.create(topic=topic, description=description)
        return redirect('/')
    else:
        return HttpResponse(render(request, 'create_page.html'))

def mainToDo(request):
    to_dos = ToDo.objects.all
    return HttpResponse(render(request, 'main_page.html', {'to_dos': to_dos}))
