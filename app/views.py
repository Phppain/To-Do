from django.shortcuts import *
from django.http import *
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
    to_dos = ToDo.objects.all()
    return HttpResponse(render(request, 'main_page.html', {'to_dos': to_dos}))

def deleteToDo(request, todo_id):
    get_object_or_404(ToDo, id=todo_id).delete()
    return redirect('/')

def editToDo(request, todo_id):
    context = get_object_or_404(ToDo, id=todo_id)

    if request.method == "POST":
        context.topic = request.POST.get('topic')
        context.description = request.POST.get('description')
        context.save()
        return redirect('/')

    return HttpResponse(render(request, 'edit_page.html', {'context': context}))
