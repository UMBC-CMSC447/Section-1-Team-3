from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class property(models.Model):
    Name = models.CharField(max_length = 30)
    Price = models.FloatField()
    Location = models.CharField(max_length = 50)
    Owner = models.CharField(max_length = 30)
    Image = models.ImageField(upload_to = '.', default = '/no-img.jpg')
    Description = models.CharField(max_length = 256)
    Rent = models.IntegerField(default = 0)
    Rating = models.IntegerField(default = 0)
    Approval = models.IntegerField(default = 0)
    RentSlots = models.TextField(null = True)
    Lat = models.FloatField(default = 38.388656, null = True)
    Long = models.FloatField(default = -75.063863, null = True)

    def __str__(self):
        return self.Name
class UserAvatar(models.Model):
    username = models.CharField(max_length = 50)
    avatar = models.ImageField(upload_to = '.', default = '/no-img.jpg')


    def __str__(self):
        return self.username
    #def create(cls,Name,Price,Location,Owner):
    #    prop = cls(Name = Name
