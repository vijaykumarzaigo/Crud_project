from .import views
from django.urls import path,include

from rest_framework import routers

from .views import Brand_po_line_item

router = routers.DefaultRouter()



router.register('brand_po_line_item',Brand_po_line_item)

urlpatterns=[
   path('',include(router.urls))
]