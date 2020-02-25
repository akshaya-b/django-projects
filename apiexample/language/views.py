from django.shortcuts import render
from rest_framework import viewsets, permissions
from .models import Language, Type, Programmer
from .serializers import LanguageSerializer, TypeSerializer, ProgrammerSerializer

class TypeView(viewsets.ModelViewSet):
    queryset= Type.objects.all()
    serializer_class= TypeSerializer

class LanguageView(viewsets.ModelViewSet):
    queryset= Language.objects.all()
    serializer_class= LanguageSerializer
    #permission_classes= (permissions.IsAuthenticatedOrReadOnly,)



class ProgrammerView(viewsets.ModelViewSet):
    queryset= Programmer.objects.all()
    serializer_class= ProgrammerSerializer

# Create your views here.
