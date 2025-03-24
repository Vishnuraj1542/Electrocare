from django.urls import path
from .views import *

urlpatterns=[
    path('userhome',UserPage.as_view(),name='userhome'),
    path('officehome',OfficePage.as_view(),name='officehome'),
    path('workerhome',WorkerPage.as_view(),name='workerpage'),
    path('adminpage',AdminPage.as_view(),name='adminpage'),
    path('login',Login.as_view(),name='loginpage'),
]