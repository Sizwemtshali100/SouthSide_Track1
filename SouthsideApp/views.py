from django.shortcuts import render, redirect, HttpResponse
from . forms import QACForms, CreateUserForm  #, QA_Agent_creation
from . models import QACModels #, QAAgent
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from . decorators import unauthenticated_user,allowed_users , Manager_only
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
import csv


# Create your views here.

@login_required(login_url='LoginPage')
@Manager_only
def Home(request):
    TheList = QACModels.objects.all()
    return render(request, 'SouthsideApp/Home.html',
                  {'TheList':TheList})

@login_required(login_url='LoginPage')
def TheForm(request):
    TheForm = QACForms
    if request.method == 'POST':
       TheForm = QACForms(request.POST)
       if TheForm.is_valid():
           TheForm.save()
           return redirect('Home')
    return render(request, 'SouthsideApp/TheForm.html',
                  {'TheForm':TheForm})

@login_required(login_url='LoginPage')
def Detail(request, List_id):
    TheList_details = QACModels.objects.get(pk=List_id)
    return render(request, 'SouthsideApp/Detail.html',
                  {'TheList_details':TheList_details})           

@login_required(login_url='LoginPage')
def Edit(request, List_id):
    TheList_details = QACModels.objects.get(pk=List_id)
    TheFormEdit = QACForms(request.POST or None, instance=TheList_details)
    if request.method == 'POST':
        if TheFormEdit.is_valid():
            TheFormEdit.save()
            return redirect('Home')
    return render(request, 'SouthsideApp/Edit.html',
                  {'TheFormEdit':TheFormEdit})  
  
@unauthenticated_user
def LoginPage(request):
    if request.method == "POST":
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        The_user = authenticate(request, username=username, password=password)

        if The_user is not None:
            login(request, The_user)
            return redirect('Home')
        else: 
            messages.info(request, 'Your username or password is incorrect!')
        
    return render(request, 'SouthsideApp/LoginPage.html',
                {})    


@login_required(login_url='LoginPage')
def RegistrationPage(request):
    if request.user.is_authenticated:
        return redirect('Home')
    else:
        RegistrationForm = CreateUserForm
        if request.method == 'POST':
            RegistrationForm = CreateUserForm(request.POST)
            if RegistrationForm.is_valid():
                user = RegistrationForm.save()  
                username = RegistrationForm.cleaned_data('username')
                group = Group.objects.get(name='Agent')
                user.groups.add(group)
                messages.success(request, "You have successfully created a new Agent!")
                return redirect('LoginPage')
        return render(request, 'SouthsideApp/RegistrationPage.html',
                    {'RegistrationForm':RegistrationForm})

@login_required(login_url='LoginPage')
def LogoutPage(request):
    logout(request)
    return redirect('LoginPage')

'''@login_required(login_url='LoginPage')
def Adding_Agent(request):
    #Agent_Adding = QA_Agent_creation
    if request.method == 'POST':
       # Agent_Adding = QA_Agent_creation(request.POST)
        if Agent_Adding.is_valid():
            Agent_Adding.save()
            return redirect('Home')
    return render(request, 'SouthsideApp/Adding_Agent.html',
                  {'Agent_Adding':Agent_Adding})
'''
@login_required(login_url='LoginPage')
#@Manager_only
def The_Agent(request):
    Agents_work = request.user
    work = QACModels.objects.filter(QA_Agent=Agents_work)
    return render(request, 'SouthsideApp/The_Agent.html',
                  {'work':work})

def Download_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['content-disposition'] = 'attachment; filename=Outcome_QA.csv'

    writer = csv.writer(response)
    Downloading_all = QACModels.objects.all()
    writer.writerow(['Date',
                     'QA_Agent',
                     'Policy_Number',
                     'Case_Number',
                    'AVS_Check',
                    'Caller_ID',
                    'Sales_Agent',
                    'Call_duration',
                    'Start_date',
                    'Premium',
                    'Debit_date',
                    'Cover_amount',
                    'QA_Correct',
                    'KPA',
                    'HIV_Required',
                    'Comment',
                    ])
    for download in Downloading_all:
        writer.writerow([download.Date,
                    download.QA_Agent,
                    download.Policy_Number,
                    download.Case_Number,
                    download.AVS_Check,
                    download.Caller_ID,
                    download.Sales_Agent,                   
                    download.Call_duration,
                    download.Start_date,
                    download.Premium,
                    download.Debit_date,
                    download.Cover_amount,
                    download.QA_Correct,
                    download.KPA,
                    download.HIV_Required,
                    download.Comment,
                    ])
    return response 


 