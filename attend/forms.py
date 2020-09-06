from django import forms
from attend.models import Attend

class AttendForm(forms.ModelForm):
        class Meta:
               model = Attend
               fields="__all__"
