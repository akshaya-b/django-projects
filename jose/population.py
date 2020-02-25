import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jose.settings')

import django
django.setup()

import random
from annan.models import AccessRecord,Website,Topic
from faker import Faker
fakegen=Faker()
topic = ['search','social','marketplace','news','games']

def add_topic():
    t=Topic.objects.get_or_create(topic=random.choice(topic))[0]
    t.save()
    return t

def populate(N=5):
    for entry in range(N):
        top=add_topic()
        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()

        webst= Website.objects.get_or_create(topic=top,url=fake_url,name=fake_name)[0]
        acc_sec = AccessRecord.objects.get_or_create(name=webst,date=fake_date)[0]

if __name__ == '__main__':
    print("populating script!")
    populate(20)
    print("populating complete!")
