from django.db import models

# Create your models here.
class Document(models.Model):
    docfile = models.FileField(upload_to='documents/%Y/%m/%d')

class Detail(models.Model):
    STATUS = (
      ('Adopted','adopted'),
      ('Available','available'),
      ('Mismatched','mismatched'),
    )
    TYPE = (
        ('Dog','dog'),
        ('Cat','cat'),
        ('Birds','birds'),
    )
    name=models.CharField(max_length=100)
    phone_no=models.CharField(max_length=10)
    address=models.CharField(max_length=100)
    email=models.EmailField(unique=True)
    description=models.TextField(max_length=200)
    status = models.CharField(
      max_length=50,
      choices=STATUS,
      default='Available',
   )
    pet_type=models.CharField(
      max_length=50,
      choices=TYPE,
      default='Dog',
   )
    pet_name = models.CharField(max_length=180,default='No Name')
