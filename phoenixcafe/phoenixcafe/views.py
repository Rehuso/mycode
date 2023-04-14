#!/usr/bin/python3

import datetime # NEW
import random

# imports from Django
from django.shortcuts import render
from django.http import HttpResponse

# This view will return "Welcome to the Phoenix Cafe!" as text
def welcome(request):
    return HttpResponse("Welcome to the Phoenix Cafe!")

# NEW
def sleepy(request):
    return HttpResponse("Z-z-z-z-z-z-z!")

# NEW date and time
def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html) # we are not returning a static string

# NEW random  number
def generateNum(request):
    randn = random.randint(0, 1000)
    return HttpResponse(f"Random number generated: {randn}")
