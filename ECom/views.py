from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def TestView(request):
    print('hi')
    return HttpResponse("hi")