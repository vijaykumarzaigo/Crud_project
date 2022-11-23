from django.urls import path,include
from.import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('crud',views.Crud_view,basename='crud')

urlpatterns = [
    path('',include(router.urls)),
]