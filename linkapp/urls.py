
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('createlink/', views.createlink, name = 'createlink'),
    path('delete/<str:id>/', views.delete, name='delete'),
    path('edit/<str:id>/', views.edit, name='edit'),

     path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
]