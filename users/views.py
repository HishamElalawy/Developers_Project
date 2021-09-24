from django.shortcuts import render , redirect
from .models import Profile
from projects.models import Project
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib import messages

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

def loginUser(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('profiles')
    if request.method == 'POST':
        username = request.POST['username'].lower()
        password = request.POST['password']
        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'Username does not exist')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username OR password is incorrect')
    
    return render(request , 'users/login-register.html')



def logoutUser(request):
    logout(request)
    return redirect('login')