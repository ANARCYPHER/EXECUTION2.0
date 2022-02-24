#from django.contrib import admin
#from django.urls import path, include

#urlpatterns = [
#    path('admin/', admin.site.urls),
#    path('', include('aapp.urls')),
#    path('associates/', include('django.contrib.auth.urls')),
#    path('associates/', include('associates.urls')),    
#]

# Configure Admin Titles
#admin.site.site_header = "Serial Administration Page"
#admin.site.site_title = "Browser Title"
#admin.site.index_title = "Welcome To The Addmin Area..."

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('aapp.urls')),    
]
