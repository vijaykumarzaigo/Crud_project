from rest_framework import serializers

from .models import Brand, Brand_PO, Document


class Brand_serializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = ['id', 'name']


class Brand_detail_serializer(serializers.ModelSerializer):
    class Meta:
        model = Brand_PO
        fields = ['id', 'brand_name','brand_po_number','po_date', 'hsn', 'name_of_certificate', 'upload_pdf_to_po', 'document']


class Brand_document(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ['id', 'document']




