from django.urls import path, re_path

from service_provider import views

urlpatterns = [
   re_path(r'.*', views.index, name='index'),
]