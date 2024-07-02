from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return render(request, 'website/index.html')

def about(request):
    #return HttpResponse("this is about page")
    return render(request,'website/about.html')

def contacts(request):
    #return HttpResponse("this is contacts")
    return render(request, 'website/contacts.html')
