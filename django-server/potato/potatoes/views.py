from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    print(request.META["HTTP_USER_AGENT"]) #print USER DATA
    return HttpResponse("hello")