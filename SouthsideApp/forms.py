from . models import QACModels  #, QAAgent
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login

class QACForms(ModelForm):
    class Meta:
        model = QACModels
        fields = ['QA_Agent','Policy_Number','Case_Number','AVS_Check','Caller_ID','Sales_Agent','Call_duration','Start_date',
                  'Premium','Debit_date','Cover_amount','QA_Correct','KPA','HIV_Required','Comment']     

        widgets = {
            'QA_Agent': forms.Select(attrs={'class':'form-control'}),
            'Policy_Number': forms.TextInput(attrs={'class':'form-control'}),
            'Case_Number': forms.TextInput(attrs={'class':'form-control'}),
            'AVS_Check': forms.Select(attrs={'class':'form-control'}),
            'Caller_ID': forms.TextInput(attrs={'class':'form-control'}),
            'Sales_Agent': forms.TextInput(attrs={'class':'form-control'}),
            'Call_duration': forms.TextInput(attrs={'class':'form-control'}),
            'Start_date': forms.TextInput(attrs={'class':'form-control'}),
            'Premium': forms.TextInput(attrs={'class':'form-control'}),
            'Debit_date': forms.TextInput(attrs={'class':'form-control'}),
            'Cover_amount': forms.TextInput(attrs={'class':'form-control'}),
            'QA_Correct': forms.Select(attrs={'class':'form-control'}),
            'KPA': forms.Select(attrs={'class':'form-control'}),
            'HIV_Required': forms.Select(attrs={'class':'form-control'}),
            'Comment': forms.Textarea(attrs={'class':'form-control'}),
        }
            

'''class QA_Agent_creation(ModelForm):
    class Meta:
        model = QAAgent
        fields = ['Agent']     

'''
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'password1': forms.Select(attrs={'class':'form-control'}),
            'password2': forms.TextInput(attrs={'class':'form-control'}),
        }

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
        widgets = {
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.TextInput(attrs={'class':'form-control'}),
            'password1': forms.Select(attrs={'class':'form-control'}),
            'password2': forms.TextInput(attrs={'class':'form-control'}),
        }        