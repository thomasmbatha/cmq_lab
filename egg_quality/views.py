from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def egg_quality(request):
    return HttpResponse("egg_index.html")
