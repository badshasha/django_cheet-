# add internal url page 


from django.urls import path
from . import views

urlpatterns = [
  path('',views.homepage, name='homepage')
]



#################################################
############  view page #########################
#################################################

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return HttpResponse("hello there friends")
