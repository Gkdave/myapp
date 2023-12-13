
from django.contrib import admin
from django.urls import path,include
from .views import * 
from django.conf import settings
from django.conf.urls.static import static 

admin.site.site_header = "Dave Webdevelopment"
admin.site.index_title = "Welcome to Dave Website"
admin.site.site_title = "Welcome to Tutorial"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home),
    path('index/',home),
    path('about/',about),
    path('services/',services),
    path("emp/",include('emp.urls'))
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
