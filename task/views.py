from django.shortcuts import render, redirect
from . import forms
from . import models
from category.models import CategoryModel
# Create your views here.
def task(request):
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST)
        if task_form.is_valid():
            task_form.save()
            return redirect('add_task')
    else:
        task_form = forms.TaskForm()
    return render(request, 'task.html', {'form' : task_form})


def edit_task(request, id):
    task = models.TaskModel.objects.get(pk=id)
    task_form = forms.TaskForm(instance=task)
    if request.method == 'POST':
        task_form = forms.TaskForm(request.POST, instance = task)
        if task_form.is_valid():
            task_form.save()
            return redirect('homepage')
    return render(request, 'task.html', {'form' : task_form})


