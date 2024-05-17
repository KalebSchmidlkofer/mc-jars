from django.shortcuts import render
from django.http import HttpResponse

def go_home(request):
  return HttpResponse("Hello, World!")