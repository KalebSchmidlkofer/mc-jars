from django.shortcuts import render
from django.http import HttpResponse

def go_home(request):
  return render(request, 'frontend/home.html')