from django.db import models
import uuid

# from djangoproject.Brand_app.models import Brand


class Po_line_item(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    line_item_id = models.CharField(max_length=256)
    # brand_name = models.ForeignKey(Brand,on_delete=models.CASCADE)
    state = models.CharField(max_length=256)
    city = models.CharField(max_length=256)
    type_quantity = models.CharField(max_length=256)
    sub_type = models.CharField(max_length=256)
    quantity = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    unit_line_price_amount = models.DecimalField(max_digits=13,decimal_places=2)
    total_amount = models.DecimalField(max_digits=13,decimal_places=2,null=True)
    comments = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
