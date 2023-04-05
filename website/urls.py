from django.urls import path
from website.views import TaskList, DetailTask, CreateTask, UpdateTask, DeleteTask, Login, Register
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path('', TaskList.as_view(), name='tasks'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('register/', Register.as_view(), name='register'),
    path('task/<int:pk>/', DetailTask.as_view(), name='task'),
    path('create_task/', CreateTask.as_view(), name='create_task'),
    path('update_task/<int:pk>/', UpdateTask.as_view(), name='update_task'),
    path('delete_task/<int:pk>/', DeleteTask.as_view(), name='delete_task'),
]
