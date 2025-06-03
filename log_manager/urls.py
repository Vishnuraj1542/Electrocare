from django.urls import path
from .views import *

urlpatterns=[
    path('admin/', admin_page,name='admin_page'),
    path('public/',public_page,name='public_page'),
    path('office/',office_page,name='office_page'),
    path('worker/',worker_page,name='worker_page'),
    path('login/',Login.as_view(),name='login')
]