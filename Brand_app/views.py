from django.shortcuts import render
from rest_framework import viewsets

from.models import Brand,Brand_PO,Document
from .pagination import StandardResultSetPagination
from.serializer import Brand_document,Brand_serializer,Brand_detail_serializer


class brand(viewsets.ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = Brand_serializer

class brand_documents(viewsets.ModelViewSet):
    queryset = Document.objects.all()
    serializer_class = Brand_document


class brand_details(viewsets.ModelViewSet):
    queryset = Brand_PO.objects.all()
    serializer_class = Brand_detail_serializer
    pagination_class = StandardResultSetPagination

