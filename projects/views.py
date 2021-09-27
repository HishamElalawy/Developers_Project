from django.shortcuts import render , redirect
from .models import Project
from .forms import ProjectForm , ReviewForm
from django.contrib.auth.decorators import login_required
from .utils import searchProjects , paginateProjects
from django.contrib import messages


def projects(request):
    projects, search_query = searchProjects(request)
    paginate_results = 3
    custom_range , projects = paginateProjects (request , projects , paginate_results)

    context = {'projects': projects,
               'search_query': search_query , 'custom_range':custom_range }
    return render(request, 'projects/projects.html', context)


def project(request , pk) :
    project = Project.objects.get(id=pk)
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.owner = request.user.profile
            review.project = project
            review.save()
            project.getVoteCount
            messages.success(request , 'Added Successfully')
            return redirect('project' , pk=project.id)
    context = {'project' : project, 'form':form}
    return render(request , 'projects/single-project.html' , context)

@login_required(login_url='login')
def createProject(request):
    profile = request.user.profile
    form = ProjectForm()
    if request.method =='POST' :
        form = ProjectForm(request.POST , request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.owner = profile
            project.save()
            return redirect('projects')
    context = {'form' : form}
    return render (request , 'projects/project-form.html' , context)

@login_required(login_url='login')
def updateProject(request , pk):
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    form = ProjectForm(instance=project)
    if request.method == 'POST' :
        form = ProjectForm(request.POST , instance=project)
        if form.is_valid():
            form.save()
            return redirect('projects')
    context = {'form' : form}
    return render(request , 'projects/project-form.html' , context)
@login_required(login_url='login')
def deleteProject(request , pk) :
    profile = request.user.profile
    project = profile.project_set.get(id=pk)
    if request.method == 'POST' :
        project.delete()
        return redirect('projects')
    context = {'object' : project}
    return render(request , 'delete-object.html' , context)
