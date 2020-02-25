from django.db import models

# Create your models here.
class City(models.Model):
    name=models.CharField(max_length=250)
    lat= models.DecimalField(null=True,max_digits=20,decimal_places=7)
    long= models.DecimalField(null=True,max_digits=20,decimal_places=7)
    main=models.CharField(max_length=250, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural='cities'
