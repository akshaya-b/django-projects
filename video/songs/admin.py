from django.contrib import admin
from . import models
# Register your models here.
class MovieAdmin(admin.ModelAdmin):
    fields =['release_year','title','length']
    search_fields=['title','release_year']
    list_filter=['release_year','length']
    list_display=['title','release_year']
    list_editable=['release_year']
admin.site.register(models.Customer)
admin.site.register(models.Movie,MovieAdmin)
