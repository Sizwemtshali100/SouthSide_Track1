from . models import QACModels  #, QAAgent
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class QACForms(ModelForm):
    class Meta:
        model = QACModels
        fields = ['QA_Agent','Policy_Number','Case_Number','AVS_Check','Caller_ID','Sales_Agent','Call_duration','Start_date',
                  'Premium','Debit_date','Cover_amount','QA_Correct','KPA','HIV_Required','Comment']     

'''class QA_Agent_creation(ModelForm):
    class Meta:
        model = QAAgent
        fields = ['Agent']     

'''
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        
