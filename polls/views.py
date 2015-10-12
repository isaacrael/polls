from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')

def polls(request):
    return render(request, 'polls.html')
