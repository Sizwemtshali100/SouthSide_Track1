from django.db import models
from django.contrib.auth.models import User

# Create your models here.

QA_Outcome = [
    ('FALSE','FALSE'),
    ('TRUE','TRUE'),
]

KPA_Outcome = [
    ('Product','Product'),
    ('Pass','Pass'),
    ('Compliance','Compliance'),
    ('Data Capturing','Data Capturing'),
    ('TCF','TCF'),

]

HIV_Test = [
    ('YES','YES'),
    ('NO','NO'),
]

AVS = [
    ('PASS', 'PASS'),
    ('FAIL', 'FAIL'),
    ('UNVERIFIED', 'UNVERIFIED'),

]
class QACModels(models.Model):
    Date = models.DateTimeField(auto_now_add=True)
    QA_Agent = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    Policy_Number = models.CharField(max_length=12)
    Case_Number = models.CharField(max_length=7)
    AVS_Check = models.CharField(choices=AVS, max_length=12)
    Caller_ID = models.CharField(max_length=50)
    Sales_Agent = models.CharField(max_length=50)
    Call_duration = models.CharField(max_length=10)
    Start_date = models.CharField(max_length=20)
    Premium = models.DecimalField(max_digits=6, decimal_places=2)
    Debit_date = models.CharField(max_length=10)
    Cover_amount = models.CharField(max_length=10)
    QA_Correct = models.CharField(choices=QA_Outcome, max_length=5)
    KPA = models.CharField(choices=KPA_Outcome, max_length=15)
    HIV_Required = models.CharField(choices=HIV_Test,  max_length=3)
    Comment = models.TextField(max_length=200)
    def __str__(self):
        return self.Policy_Number
   
