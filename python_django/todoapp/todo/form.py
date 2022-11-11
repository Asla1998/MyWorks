from models import TodoTask
from django import forms


class TodoForm(forms.ModelForm):
    class Meta:
        Model=TodoTask
        fields=['taskname','category','priority','date']
