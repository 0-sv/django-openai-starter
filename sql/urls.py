from django.urls import path

from sql import views

urlpatterns = [
    path('', views.index, name='index'),
]