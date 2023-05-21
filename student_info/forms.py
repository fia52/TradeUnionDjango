from django.forms import ModelForm
from .models import Student
from django import forms


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        widgets = {
            'myfield': forms.TextInput(attrs={'class': 'myfieldclass'}),
        }
