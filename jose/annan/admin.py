from django.contrib import admin
from annan.models import Topic,AccessRecord,Website
# Register your models here.
admin.site.register(Topic)
admin.site.register(Website)
admin.site.register(AccessRecord)


##create super user
##python manage.py createsuperuser
##username: jose
##mail:akshayabaskaran1996@gmail,com
##password:jose
