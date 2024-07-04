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

def details(request,domain_id):
    projects = get_object_or_404(developer,pk=domain.id)
    return render(request, 'web/detail.html', {'projects': projects})