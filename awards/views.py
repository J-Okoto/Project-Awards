from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Post,Profile,Rating
from .forms import ProfileForm
import datetime as dt
from django.http import JsonResponse
import json
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/accounts/login/')
def welcome(request):
    return render(request, 'index.html')

def search_results(request):
    
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