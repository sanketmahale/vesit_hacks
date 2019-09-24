from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('login',views.login,name ='login'),
    path('signup',views.signup,name='signup'),
    path('',views.home,name='home'),  
    path('employee',views.emp,name='employee'),
    path('rating',views.rating,name = 'rating'),
    path('projectForm',views.projectForm,name='project'),
    path('teamLeader',views.teamLeader,name='leader')   
]
