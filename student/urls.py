from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('insert', views.insert),
    path('empfatdata', views.empfatdata),
    path('done', views.done),
    path('', views.home),
    path('qr', views.insertqr),
    path('insertqr', views.insertqr),
    path('updateqr', views.updateqr),
   ]

