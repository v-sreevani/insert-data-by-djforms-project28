from django import forms
from app.models import *
class StudentForm(forms.Form):
    sid=forms.IntegerField()
    name=forms.CharField(max_length=100)
    email=forms.EmailField()

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'