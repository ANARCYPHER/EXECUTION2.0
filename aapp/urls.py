#from django.urls import path
#from . import views

#urlpatterns = [    
#    path('', views.index, name="index"),
#   path('about', views.about, name="about"),
#   path('doxing', views.doxing, name="doxing"),
#   path('add_serial', views.add_serial, name='add-serial'),
    #path('search_aapp', views.search_aapp, name='search-aapp'),
    #path('search_autopsypro', views.search_autopsypro, name='search-autopsypro'),         
#]
from django.urls import path
from . import views

urlpatterns = [
     path('', views.index, name="index"),
]   