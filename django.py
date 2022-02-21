# send object with template
#################################################
############  view page #########################
#################################################

from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.




def homepageNew(request):
    return render(request,'appname/templatge.html' , {'key' :1234})        # {{ key }}        [access using this ]                     