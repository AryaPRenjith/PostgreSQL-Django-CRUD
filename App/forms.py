from socket import fromshare
from django import forms
from App.models import EmpModel

class EmpForm(forms.ModelForm):
    class Meta: 

        model=EmpModel
        # fields=['id','empname','email','occupation','salary','gender']
        fields='__all__'