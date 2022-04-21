from django import views


from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_data),
    path('add', views.addClass),
    path('update', views.updateClass),
    path('login', views.loginUser),
    path('signup', views.signupUser),
]