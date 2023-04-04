from django.urls import path
from website.views import TaskList, DetailTask, CreateTask, UpdateTask, DeleteTask

urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('task/<int:pk>/', DetailTask.as_view(), name='task'),
    path('create_task/', CreateTask.as_view(), name='create_task'),
    path('update_task/<int:pk>/', UpdateTask.as_view(), name='update_task'),
    path('delete_task/<int:pk>/', DeleteTask.as_view(), name='delete_task'),
]
