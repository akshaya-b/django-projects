# Generated by Django 2.2.6 on 2019-11-30 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mapapp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='lat',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='long',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='city',
            name='main',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
