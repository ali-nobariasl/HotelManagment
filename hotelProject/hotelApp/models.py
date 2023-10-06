from django.db import models
from django.conf import settings

class Room(models.Model):
    roomnumber = models.PositiveIntegerField()
    capacity = models.PositiveIntegerField()
    bednumber = models.PositiveIntegerField()
    price = models.FloatField()
    availability = models.BooleanField(default=True)
    #checkin_date = models.DateTimeField()
    #checkout_date = models.DateTimeField()
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    
    categories = (
        ('stn','standard'),
        ('lux','luxury'),
        ('slx','superluxury'),
    )
    category = models.CharField(max_length=3, choices = categories , default= 'stn')
    


    def __str__(self):
        return str(self.roomnumber) + " , " + str(self.capacity)+ " , " + str(self.bednumber) 



class Book(models.Model):
    
    extra_benefits = (
        ('Room Service','Room Service'),
        ('Breakfast','Breakfast'),
        ('Lunch','Lunch'),
        ('Entertainment','Entertainment'),

    )
    benefit = models.CharField(max_length=20,choices=extra_benefits, null=True, blank=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    room = models.ForeignKey(Room,on_delete= models.CASCADE)
    checkin_date = models.DateTimeField()
    checkout_date = models.DateTimeField()
    
    
    def __str__(self):
        return str(self.checkin_date) + " , " + str(self.checkout_date)