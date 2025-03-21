from django.shortcuts import render
from django.http import HttpResponse

def welcome(request):
    return HttpResponse("Hey,This is a Sample!")
def sampleapp_home(request):
    return HttpResponse("Welcome to my SampleApp!")


