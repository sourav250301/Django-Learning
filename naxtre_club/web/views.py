from django.shortcuts import render

# Create your views here.
def webin(request):
    return render(request,'web/webin.html')