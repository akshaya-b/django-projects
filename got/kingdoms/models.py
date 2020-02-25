from django.db import models
from django.urls import reverse

# Create your models here.
class Region(models.Model):
    name= models.CharField(max_length=256)
    climate = models.CharField(max_length=256)

    def _str_(self):
        return self.name


    def get_absolute_url(self):
        return reverse("kingdoms:detail",kwargs={'pk':self.pk})


class Kingdom(models.Model):
    name= models.CharField(max_length=256)
    king= models.CharField(max_length=256)
    flag= models.CharField(max_length=256)
    reg= models.ForeignKey(Region, related_name='kingdom',on_delete=models.DO_NOTHING,null=True, blank=True)

    def _str_(self):
        return self.name
