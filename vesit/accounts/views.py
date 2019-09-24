from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User,auth
from django.contrib.auth import authenticate

# Create your views here.

def login(request):

    if request.method == 'POST' : 
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username,password=password)
        print(user)
        if user is not None : 
            auth.login(request,user)
            Profiles = Profile.objects.all()
            for p in Profiles :
                if(user.pk==p.user_id):
                    position = p.position
            print(position)
            if(position == "Employee"):
                return redirect('employee')
            if(position == "Team Head"):
                return render(request,'accounts/Team_Leader.html')
            if(position == "Head Supervisor"):
                return render(request,'headSupervisor/teamDash.html')
        else :
            return redirect('/')
    else:
        return render(request,'accounts/Login.html')

def signup(request):
        if request.method == 'POST' : 
            teams = Teams.objects.all()
            name = request.POST['Name']
            email = request.POST['email']
            password = request.POST['password'] 
            position = request.POST.get('position')
            teamNameVar = request.POST.get('team', 'Tech') 
            for team in teams:
                if (team.pk == teamNameVar):
                    teamObject = team
            user = User.objects.create_user(username=name,password=password,email=email)
            user.save()
            profile = Profile.objects.create(user = user, name = name,teamId = team, position = position)
            profile.save()
            print("User created")
            return redirect('/')
        else:
            teams = Teams.objects.all()
            return render(request,'accounts/signup.html',{'teams':teams})

def home(request): 
    teams = Teams.objects.all()
    return render(request,'home.html',{'teams':teams})
    
def emp(request):
    return render(request,'accounts/emp.html')

def rating(request):
    return render(request,'accounts/ratingForm.html')

def projectForm(request):
    return render(request,'accounts/projectForm.html')

def teamLeader(request):
    return render(request,'accounts/Team_leader.html')