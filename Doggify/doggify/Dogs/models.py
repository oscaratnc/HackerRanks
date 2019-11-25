from django.db import models

# Create your models here.
#PErro adopcion carrrito 

class Dog(models.Model):
    name  = models.TextField(max_length=50) 
    age =  models.IntegerField()
    gender = models.BooleanField()
    size =  models.DecimalField(decimal_places=2)
    breed =  models.CharField(max_length = 3, choices = [
        ("BTR", 'Boston Terrier'),
        ("BOX", 'Boxer'),
        ("CHW", 'ChowChow'),
        ("PUG", 'Pug'),
    ])
 
class Adoption(models.Model):
    dog = models.ForeignKey(Dog, on_delete=models.DO_NOTHING)
    user = mode

class Wishlist(models.Model):

class Shelter(models.Model):
  