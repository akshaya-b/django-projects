from django.db import models
class Family(models.Model):
    girl= models.CharField(max_length=255, unique=True)
    boy=models.CharField(max_length=255, unique=True)
    husky=models.CharField(max_length=255)
    goldie=models.CharField(max_length=255)





# Create your models here.
