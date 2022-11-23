from django.db import models
import uuid
# Create your models here.
select_country = (
                ('mumbai','mumbai'),
                ('hyderabad','hyderabad'),
                ('chennai','chennai'),
                ('bangalore','bangalore'),
                ('andhrapradesh','andhrapradesh'),
                )

class api_model(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False)
    name = models.CharField(max_length=256)
    profile_picture = models.ImageField(upload_to='media')
    country = models.CharField(choices=select_country,max_length=256,blank=False)