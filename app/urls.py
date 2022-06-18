from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    
    path('register/', views.register, name='register'),
    
    path('login/', views.user_login, name='login'),
    
    path('logout/', views.user_logout, name='logout'),
    
    path('profile/', views.user_profile, name='profile'),
    
    path('update_profile/', views.update_profile, name ='update'),
    
    path('add_post/', views.user_post, name ='add_post'),
    
    path('add_business/', views.create_business, name ='business'),
    
    path('add_neighbourhood/', views.create_hood, name='neighbourhood'),
    
    path('hoods/', views.view_hoods, name ='hoods'),
    
]
