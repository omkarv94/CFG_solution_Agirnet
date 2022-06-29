from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("", views.index, name ='home'),
    path("login", views.login, name ='login'),
    path("registration", views.registration, name ='register'),
    path("form/<str:pk>/",views.form,name='form'),
    
    path("dash", views.dash, name ='dash'),
    path("about", views.about, name ='about'),
   
    path("homepage", views.homepage, name ='homepage'),
    path("activityreplit", views.activityreplit, name='activityreplit'),
    
    path("contact", views.contact, name ='contact'),
    path("pd", views.pd, name ='pd'),
    path("analytics", views.analytics, name ='analytics'),
    
    #path("form2/<str:pk>/",views.form2,name='form2'),
]