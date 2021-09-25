from django.shortcuts import render , redirect
from .models import Profile
from projects.models import Project
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm , EditAccountForm
from django.contrib.auth.decorators import login_required
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
@login_required(login_url='login')
def userAccount(request):
    profile = request.user.profile
    skills = profile.skill_set.all()
    projects = profile.project_set.all()
    context = {'profile':profile , 'skills':skills , 'projects':projects}
    return render(request , 'users/account.html' , context)

@login_required(login_url='login')
def editUserAccount(request):
    profile = request.user.profile
    form = EditAccountForm(instance=profile)
    if request.method =='POST':
        form = EditAccountForm(request.POST , request.FILES ,instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = profile.username.lower()
            profile.save()
            messages.success(request , 'your Account Has been updated')
            return redirect('account')
        else:
            messages.error(request , 'Faild To Update The User')
    context = {'profile':profile , 'form':form}
    return render(request , 'users/edit-account.html' , context)

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
            return redirect('profile')
        else:
            messages.error(request, 'Username OR password is incorrect')
    
    return render(request , 'users/login-register.html')



def logoutUser(request):
    logout(request)
    return redirect('login')


def registerUser(request):
    page = 'register'
    form = CustomUserCreationForm()

    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user)
            return redirect('profiles')

        else:
            messages.error(
                request, 'An error has occurred during registration')

    context = {'page': page, 'form': form}
    return render(request, 'users/login-register.html', context)