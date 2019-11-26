from django.db import models
from django.contrib.auth.models import User

class Dog(models.Model):
    name  = models.TextField(max_length=50) 
    age =  models.IntegerField()
    gender = models.BooleanField()
    size =  models.DecimalField(decimal_places=2)
    photo = models.TextField(max_length=50)
    breed =  models.CharField(max_length = 3, choices = [
        ("BTR", 'Boston Terrier'),
        ("BOX", 'Boxer'),
        ("CHW", 'ChowChow'),
        ("PUG", 'Pug'),
    ])

class Adoption(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.DO_NOTHING)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    shelter = models.ForeignKey(Shelter, on_delete=models.DO_NOTHING)
    adoption_date = models.DateTimeField(auto_now= True)

class Shelter(models.Model):
    name  =  models.TextField(max_length= 20)
    owner = models.TextField(max_length= 30)
    address = models.TextField(max_length= 60)
    phone = models.TextField(max_length=10)

  