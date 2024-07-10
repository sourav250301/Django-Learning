from email.policy import default
from django.db import models
from django.utils import timezone

# Create your models here.

class developer(models.Model):
    DOMAIN_CHOICE = [
        ('R', 'React'),
        ('A', 'Angular'),
        ('N', 'Node'),
        ('P', 'Python'),
        ('D', 'Database'),
    ]
    name= models.CharField(max_length=100)
    image = models.ImageField(upload_to='media/club/')
    date_joined = models.DateField(auto_now=False, auto_now_add=False)
    type= models.CharField(max_length=2, choices = DOMAIN_CHOICE)
    projects = models.TextField(default="")

    def __str__(self):
        return self.name
    
    class ratings(models.Model):
        Star_Choice= [
            ('A', 'Top Perfomer'),
            ('B', 'Team Worker'),
            ('C', 'Not up to Mark'),
        ]
        rate =models.CharField(max_length=1, choices= Star_Choice)
        review =models.TextField(default="")
    