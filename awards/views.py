from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from .models import Project,Profile,Rating,countries
from .forms import ProfileForm
import datetime as dt
from django.http import JsonResponse
import json
from django.contrib.auth.models import User
from django.contrib import auth, messages
from .forms import *
from .models import *

# Create your views here.

def welcome(request):
    return render(request, 'index.html')
