from django import forms
from .models import *
class NotesForm(forms.ModelForm):
    class Meta:
        model =Notes
        fields=['title','description']
class DateInput(forms.DateInput):
    input_type='date'        
class Homeworform(forms.ModelForm):
    class Meta:
        model=Homework
        widgets={'due':DateInput()}
        fields=['subject','title','description','due','is_finished']
class DashboardFom(forms.Form):
    text=forms.CharField(max_length=100,label="Enter Yor Search:") 