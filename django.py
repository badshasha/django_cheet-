# most use full libs for authentication 

from django.shortcuts import render , get_object_or_404 , redirect
from django.http import HttpResponse
from django.contrib.auth.models import  User
from django.contrib.auth.forms import  UserCreationForm
from  django.contrib.auth import login , logout
from django.db import IntegrityError

# how to log in 

def todopage(request):
    error = None
    if request.method == "POST":
        if request.POST["password1"] == request.POST["password2"]:
            if request.POST["username"]:
                try:
                    user = User.objects.create_user(request.POST["username"], email=None, password=request.POST["password1"])  # new user create 
                    user.save()  # user save in the database
                    
                    login(request,user)  # log in function 
                    
                    return redirect('todo:todoall') # redirect 
                except IntegrityError:
                    error = "user name not available [please try different user name]"
            else:
                error = "empty user name not allowed"
        else:
            error = "password and confirm password are not matching"

    return render(request, 'todo/todoHomepage.html', {'form': UserCreationForm(), 'error': error})
