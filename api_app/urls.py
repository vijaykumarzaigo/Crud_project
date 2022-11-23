from django.urls import path
from.import views


urlpatterns=[
    # API Class based view
    path('api',views.Api_create_read.as_view(),name='api'),
    path('api/<pk>',views.Api_read_update_delete.as_view(),name='api'),

    # Api function based view
    path('api_view_create',views.Api_view_create),
    path('api_view_list',views.Api_view_list),
    path('api_view_retrieve/<pk>',views.Api_view_retrieve),
    path('api_view_update/<pk>',views.Api_view_update),
    path('api_view_delete/<pk>',views.Api_view_delete),
]