from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home, name='Home'),
    path('TheForm/', views.TheForm, name='TheForm'),
    path('Detail/<int:List_id>', views.Detail, name='Detail'),
    path('Edit/<int:List_id>', views.Edit, name='Edit'),
    path('LoginPage/', views.LoginPage, name='LoginPage'),
    path('LogoutPage/', views.LogoutPage, name='LogoutPage'),
    path('RegistrationPage/', views.RegistrationPage, name='RegistrationPage'),
    path('The_Agent/', views.The_Agent, name='The_Agent'),
    #path('Adding_Agent/', views.Adding_Agent, name='Adding_Agent'),


]
