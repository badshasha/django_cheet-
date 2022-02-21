# load pagewtih render 
#################################################
############  view page #########################
#################################################

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def homepage(request):
    return HttpResponse("hello there friends")


def homepageNew(request): #---------------------------------------------------------->  create folder 
    return render(request,'appname/templatge.html')                                    #  templates > appName > templatepage.html