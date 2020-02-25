from django.db import models

## python manage.py migrate
##python manage.py makemigrations appname
## python manage.py migrate
##python manage.py shell
##from annan.models import Topic
##print(Topic.objects.all())
##t=Topic(topic="annan python bootcamp")
##t.save()
##print(Topic.objects.all())
##quit()


# Create your models here.
class Topic(models.Model):
    topic=models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.topic

class Website(models.Model):
    topic= models.ForeignKey(Topic,on_delete=models.DO_NOTHING,)
    name= models.CharField(max_length=200, unique=True)
    url= models.URLField(max_length=200, unique=True)

    def __str__(self):
        return self.name

class AccessRecord(models.Model):
    name=models.ForeignKey(Website,on_delete=models.DO_NOTHING,)
    date=models.DateField()

    def __str__(self):
        return str(self.date)
