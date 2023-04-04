from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from website.forms import TaskForm
from website.models import Task
from django.urls import reverse_lazy

# A class view is a class that inherits from one of the generic views in Django. It is used to display a list of objects.

# By default, Django will look for a template called <app name>/<model name>_list.html.
# In this case, it will look for a template called website/task_list.html. If you want to change the name of the template,
# you can specify the template_name attribute.

# Object_list is the name of the context variable that will be used in the template to access the list of objects,
# we can change it by specifying the context_object_name attribute.


class TaskList(ListView):
    model = Task
    context_object_name = 'tasks'
    template_name = 'website/task_list.html'
    
class DetailTask(DetailView):
    model = Task
    template_name = 'website/task_detail.html'
    context_object_name = 'task'

class CreateTask(CreateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
class UpdateTask(UpdateView):
    model = Task
    fields = '__all__'
    success_url = reverse_lazy('tasks')
    
class DeleteTask(DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    template_name = 'website/task_delete.html'
    