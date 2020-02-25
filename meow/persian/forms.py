from django import forms
from persian.models import Family
# from django.forms import ModelForm

class Familyform(forms.ModelForm):
    class Meta():
        model=Family
        fields= ('girl','boy','husky','goldie')
