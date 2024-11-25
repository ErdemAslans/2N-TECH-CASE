from django.urls import path
from . import views

app_name = 'personel'

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
]