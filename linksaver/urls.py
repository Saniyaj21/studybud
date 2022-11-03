
from django.contrib import admin
from django.urls import path,include
from linkapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('linkapp.urls')),
]
