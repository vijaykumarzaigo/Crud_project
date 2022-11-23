from django.urls import path
from.import views


urlpatterns=[
    # API Class based view
    path('api',views.api_create_read.as_view(),name='api'),
    path('api/<pk>',views.api_read_update_delete.as_view(),name='api'),

    # Api function based view
    path('api_view_create',views.api_view_create),
    path('api_view_list',views.api_view_list),
    path('api_view_retrieve/<pk>',views.api_view_retrieve),
    path('api_view_update/<pk>',views.api_view_update),
    path('api_view_delete/<pk>',views.api_view_delete),
]