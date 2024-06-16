from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('bookadd/',views.add_book,name='bookadd'),
    path('', views.home, name='home'),  # Define your home view
]