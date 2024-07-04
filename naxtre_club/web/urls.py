from django.urls import path
from . import views

urlpatterns = [
    path('',views.webin,name='webin'),
    path('<int:id>/',views.details,name='details'),
]
