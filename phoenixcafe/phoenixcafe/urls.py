#!/usr/bin/python3

# imports from Django
from django.contrib import admin
from django.urls import path
from .import views

urlpatterns = [
    path('welcome/', views.welcome),
    # custom path
    path('sleepy/', views.sleepy),
    # custom path rand number
    path('generateNum/', views.generateNum),
]


# NEW - clock/ is the path to trigger our fuction
urlpatterns += [path('clock/', views.current_datetime),]
