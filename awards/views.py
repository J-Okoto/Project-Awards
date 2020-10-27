from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Project,Profile,Rating,Countries
# from .forms import ProfileForm
import datetime as dt
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .forms import *
from .models import *

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    return render(request, 'index.html')

def search_results(request):
    current_user = request.user
    profile =Profile.objects.get(username=current_user)
    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_project(search_term)
        message=f"{search_term}"

        print(searched_projects)

        return render(request,'search.html',{"message":message,"projects":searched_projects,"profile":profile})

    else:
        message="You haven't searched for any term"
    return render(request,'search.html',{"message":message})

def create_profile(request):
    current_user = request.user
    if request.method=='POST':
        form = ProfileForm(request.POST,request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.username = current_user

            profile.save()
        return redirect('welcome')
    else:
        form=ProfileForm()

    return render(request,'create_profile.html',{"form":form})

def profile(request):
    current_user = request.user
    profile =Profile.objects.get(username=current_user)
    projects=Project.objects.filter(username=current_user)

    return render(request,'profile.html',{"projects":projects,"profile":profile})

def new_project(request):
    current_user = request.user
    profile =Profile.objects.get(username=current_user)
    if request.method =='POST':
        form = ProjectForm(request.POST,request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.username = current_user
            project.avatar = profile.avatar
            project.country = profile.country

            project.save()
    else:
        form = ProjectForm()

    return render(request,'new_project.html',{"form":form})

