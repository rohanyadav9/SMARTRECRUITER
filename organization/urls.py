from django.urls import path
from . import views


urlpatterns=[
    path('login',views.login,name='login'),
    path('logup',views.logup,name='logup'),
    path('com_details',views.com_details,name='com_details'),
    path('emp',views.emp,name='emp'),
    
]