from django import forms
from django.forms import ModelForm 
from website.models import Task


class TaskForm(ModelForm):
    title = forms.CharField(max_length=100)
    description = forms.Textarea()
    completed = forms.BooleanField(required=False)

    class Meta:
        model = Task
        fields = '__all__'
