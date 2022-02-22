# send object with template
#################################################
############  view page #########################
#################################################

from django.shortcuts import render
from django.http import HttpResponse
import numpy as np

# Create your views here.



def formpost(request):
    length_of_post = request.POST['length']  # one way to doing it 
    value = "".join([ str(np.random.random_integers(10)) for _ in range(int(length_of_post))])
    print(value)
    return render(request, 'generator/password.html',{'gen':value})



# or use this thing 
     length_of_post = request.POST.get('length')