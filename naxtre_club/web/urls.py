from django.urls import path
from . import views

urlpatterns = [
    path('',views.webin,name='webin'),
    path('<int:domain_id>/',views.details,name='details'),
]
