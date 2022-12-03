from rest_framework import routers
from.import views
from django.urls import path,include

from .views import brand, brand_details, brand_documents

router = routers.DefaultRouter()
router.register('brand',brand)
router.register('brand_details',brand_details)
router.register('brand_documents',brand_documents)

urlpatterns=[
    path('',include(router.urls))
]