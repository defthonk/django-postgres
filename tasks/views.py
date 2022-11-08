from django.shortcuts import render, redirect
from .models import task

# Create your views here.
def list_tasks(request):
    tasks = task.objects.all()
    return render(request, 'list_tasks.html', {"tasks": tasks})

def create_task(request):
    Task = task(title=request.POST['title'], description=request.POST['description'])
    Task.save()
    #print(request.POST['description'])
    return redirect('/tasks/')

def delete_task(request, task_id):
    delete_task = task.objects.get(id=task_id)
    delete_task.delete()
    return redirect('/tasks/')
