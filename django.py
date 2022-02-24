# most use full libs for authentication 

from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse
from django.contrib.auth.models import  User
from django.contrib.auth.forms import  UserCreationForm
from  django.contrib.auth import login , logout
from django.db import IntegrityError

# how to logout


def todologout(request):
    if request.method == "POST":
        logout(request)
        return redirect('todo:todohomepage')

