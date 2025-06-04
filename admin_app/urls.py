from django.urls import path
from .views import *

urlpatterns = [
    path('office_registration/',OfficeRegistration.as_view(),name='office_registration')
]