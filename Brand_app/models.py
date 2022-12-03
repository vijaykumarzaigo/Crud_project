from django.db import models
import uuid

from django.utils import timezone



class Brand(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=256)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)


class Document(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    document = models.CharField(max_length=256)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

class Brand_PO(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    brand_name = models.ForeignKey(Brand,on_delete=models.CASCADE)
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    brand_po_number = models.CharField(max_length=256)
    po_date = models.DateField()
    supplier_number = models.CharField(max_length=256,blank=True)
    payment_term = models.TextField(blank=True)
    shipping_term = models.TextField(blank=True)
    mailing_address = models.CharField(max_length=256,blank=True)
    hsn = models.CharField(max_length=256)
    name_of_certificate = models.CharField(max_length=256,)
    upload_pdf_to_po = models.ImageField(upload_to='media')

    updated_by = models.CharField(max_length=256, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)




