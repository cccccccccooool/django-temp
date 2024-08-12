from django.urls import path
from app01 import views
urlpatterns = [
    path('', views.index),
    path('1/', views.getElemt),
    path('ip/',views.print_ip)
]
