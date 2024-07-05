from django.shortcuts import render
from .models import developer
from django.shortcuts import get_object_or_404

# Create your views here.
def webin(request):
    domains = developer.objects.all()
    return render(request,'web/webin.html', {'domains': domains})

def details(request,domain_id):
    projects = get_object_or_404(developer,pk=domain_id)
    return render(request, 'web/detail.html', {'projects': projects})

def ratings(request,user_id):
    reviews = ratings.object.all()
    return render(request, 'web/detail.html', {'reviews':reviews})