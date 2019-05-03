# pages/urls.pyS
from django.conf.urls import url, include

from . import views

urlpatterns = [
    
  
    url(r'^$', views.homes, name='home'),
    url(r'^signIn/', views.signIn),
    url(r'^Clients/', views.clients, name='Clients'),
    #url(r'^Project/', views.abouts, name='Projects'),
    url(r'^Projects/', views.projects, name='Projects'),
      url(r'^addClient/', views.addClient),
      url(r'^addProject/', views.addProject),
      url(r'^editClient/', views.editClient),
       url(r'^editProject/', views.editProject),
       url(r'^deleteClient/', views.deleteClient),
       url(r'^deleteProject/', views.deleteProject),
   
    
      
  
       
    
]