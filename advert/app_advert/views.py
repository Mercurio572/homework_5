from django.shortcuts import render
from django.http import HttpResponse
# from .models import Advertisment
# from .forms import Advertisement

def index(request):
    return render(request, 'index.html')

def top_sellers(request):
    return render(request, 'top-sellers.html')

# Create your views here.
