from django.shortcuts import render , redirect
from .models import Profile
from projects.models import Project

def profiles(request):
    profiles = Profile.objects.all()
    context = {'profiles':profiles}
    return render(request , 'users/profiles.html' , context)

def userProfile(request , pk):
    profile = Profile.objects.get(id=pk)
    topSkills = profile.skill_set.exclude(description='')
    otherSkills = profile.skill_set.filter(description='')
    projects = profile.project_set.all()
    context = {'profile' : profile , 'topSkills' : topSkills ,'otherSkills' : otherSkills ,'projects':projects }
    return render (request , 'users/user-profile.html' , context)