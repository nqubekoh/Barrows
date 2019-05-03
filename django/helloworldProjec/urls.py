
# pages_project/urls.py

from django.conf.urls import  url, include
from django.contrib import admin


admin.autodiscover()

urlpatterns = [

    url(r'^admin/',  admin.site.urls),
  
     url(r'^', include('pages.urls')), # new


         
]
    
