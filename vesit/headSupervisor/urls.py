from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.amit,name = 'headSupervisor'),
    path('teamProgress',views.teamProgress,name='teamProgress'),
    path('teamPStructure',views.teamStructure,name='teamStructure')
]