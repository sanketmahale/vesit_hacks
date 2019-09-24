from django.db import models
from datetime import date
# Create your models here.

class Teams(models.Model):
    teamName = models.CharField(max_length = 200)
    teamLeader =  models.ForeignKey('auth.User', on_delete = models.PROTECT)
    time = models.DateField(("Date"), default= date.today)

class Profile(models.Model):
    Employee = 'Employee'
    TeamHead = 'Team Head'
    HeadSupervisor = 'Head Supervisor'
    Supervisor = 'Supervisor'
    POSITION_CHOICES = (
        (Employee, 'Employee'),
        (Supervisor, 'Supervisor'),
        (TeamHead, 'Team Head'),
        (HeadSupervisor, 'Head Supervisor'),
    )
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    name = models.CharField(max_length = 20)
    teamId = models.ForeignKey(Teams, on_delete = models.PROTECT)
    position = models.CharField(
    max_length=20,
    choices=POSITION_CHOICES, default = Employee
    )

    def __str__(self):
        return self.user

class Projects(models.Model):
    teamid = models.ForeignKey(Teams,on_delete = models.CASCADE)
    title = models.CharField(max_length=20)
    desc = models.TextField(max_length = 500)
    deadline = models.DateField(("Date"), default=date.today)
    def __str__(self):
        return self.title

class ProjectReport(models.Model):
    teamid = models.ForeignKey(
     Teams,on_delete = models.CASCADE)
    time = models.DateField(("Date"), default=date.today)
    pid = models.ForeignKey(Projects,on_delete=models.CASCADE)
    cumulativeRating = models.DecimalField(decimal_places = 2, max_digits = 3,default = 0)


class UserReport(models.Model):
    time = models.DateField(("Date"), default = date.today)
    projectid= models.ForeignKey(Projects, on_delete=models.CASCADE)
    empid= models.ForeignKey('auth.User', on_delete=models.CASCADE)
    teamid= models.ForeignKey(Teams, on_delete=models.CASCADE)
    description = models.TextField(max_length=500)
    contribution = models.TextField(max_length=500)
    approach = models.TextField(max_length=500)
    rating = models.DecimalField(decimal_places = 2, max_digits = 3,default = 0)