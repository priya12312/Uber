from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length = 15,null = True,blank = True)
    surname = models.TextField(max_length = 15,null = True,blank = True)
    birth = models.DateField(max_length = 10,null = True,blank = True)
    mobile = models.IntegerField(max_length = 10,null = True,blank = True)
    GENDER_TYPE = (
        (1, 'Male'),
        (2, 'Female'),
        (3, 'Other'),
    )
    gender_type = models.IntegerField(
        choices = GENDER_TYPE,
    )
class Orders(models.Model):
    name = models.CharField(max_length = 15,null = True,blank = True)
    price = models.IntegerField(max_length = 15,null = True,blank = True)
    discount = models.IntegerField(max_length = 15,null = True,blank = True)
    quantity = models.IntegerField(max_length = 15,null = True,blank = True)
    address = models.TextField(max_length = 15,null = True,blank = True)
    place_at = models.DateField(max_length = 15,null = True,blank = True)