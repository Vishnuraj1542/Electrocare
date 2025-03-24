from django.urls import path
from .views import OfficeRegistration
urlpatterns=[
    path('officeregistration/',OfficeRegistration.as_view(),name='office_registration')
]