
# path with route id 

from django.urls import path
from . import views

urlpatterns = [
    path('',views.gloghome,name='blogHomePage'),
    path('<int:blog_id>/' , views.selectedBlogPage , name='selectePage'),

]


# views page 

def selectedBlogPage(request,blog_id):
    return render(request , 'blog/selected.html')
