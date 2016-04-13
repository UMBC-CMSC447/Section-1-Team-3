from django.db import models

# Create your models here.
class property(models.Model):
    Name = models.CharField(max_length = 30)
    Price = models.FloatField()
    Location = models.CharField(max_length = 50)
    Owner = models.CharField(max_length = 30)

    def __str__(self):
        return self.Name
    #def create(cls,Name,Price,Location,Owner):
    #    prop = cls(Name = Name
