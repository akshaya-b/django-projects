# Generated by Django 2.2.6 on 2019-11-12 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Family',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('girl', models.CharField(max_length=255, unique=True)),
                ('boy', models.CharField(max_length=255, unique=True)),
                ('husky', models.CharField(max_length=255)),
                ('goldie', models.CharField(max_length=255)),
            ],
        ),
    ]
