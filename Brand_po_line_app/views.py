from django.shortcuts import render
from .pagination import StandardResultSetPagination
from.models import Po_line_item
from.serializer import Brand_po_line_item_serializer
from rest_framework import viewsets


class Brand_po_line_item(viewsets.ModelViewSet):
    queryset = Po_line_item.objects.all()
    serializer_class = Brand_po_line_item_serializer
    pagination_class = StandardResultSetPagination
