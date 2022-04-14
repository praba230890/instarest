from django.urls import path

from service_creator import views

urlpatterns = [
    path('', views.index),
]