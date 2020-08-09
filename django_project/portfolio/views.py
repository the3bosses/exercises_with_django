from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  return render(request, 'portfolio/index.html')

def about(request):
  return HttpResponse('<h1>About</h1>')
