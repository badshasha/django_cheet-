# watch image on site 

# setting file 
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'



# url maning page
from django.conf.urls.static import static
from django.conf import settings

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

