from django.contrib import admin
from .models import * 

myModels = [Teams,Profile,Projects,ProjectReport,UserReport]  # iterable list
admin.site.register(myModels)