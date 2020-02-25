from django.db import models

class Type(models.Model):
    name=models.CharField(max_length=250)
    def __str__(self):
        return self.name

class Language(models.Model):
    name= models.CharField(max_length=250)
    type= models.ForeignKey(Type,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

class Programmer(models.Model):
    name= models.CharField(max_length=250)
    languages=models.ManyToManyField(Language)
    def __str__(self):
        return self.name
