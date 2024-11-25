from django.urls import path
from . import views

app_name = 'yetkili'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
]
