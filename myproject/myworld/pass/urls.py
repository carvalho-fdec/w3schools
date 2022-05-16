from django.urls import path
from . import views

urlpatterns = [
    path('', views.passcheck, name='passcheck'),
    path('add/', views.add, name='add'),
    path('logincheck/', views.logincheck, name='logincheck'),
]
