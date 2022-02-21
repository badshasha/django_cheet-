# add new url file
# add it's to main url page 


from django.urls import path , include

urlpatterns = [
    path('',include("generator.urls"))  # bofore creating the link please create the url link other wise it's not working 
]