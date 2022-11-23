from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from.models import crud_model
from.serializer import crud_serializer
# Create your views here.


class crud_view(ModelViewSet):
    serializer_class = crud_serializer
    queryset = crud_model.objects.all()
