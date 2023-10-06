from django.db import models
from django.contrib.auth.models import User


class Guest(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=30)
    lastname= models.CharField(max_length=30)
    email = models.EmailField(max_length=100, unique=True)
    birth_date = models.DateTimeField(null=True, blank=True)
    #checkin_date = models.DateTimeField(null=True, blank=True)
    
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
    