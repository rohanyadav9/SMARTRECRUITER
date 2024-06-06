from django.urls import path
from . import views


urlpatterns=[
    path('signin',views.signin,name='signin'),
    path('signup',views.signup,name='signup'),
    path('matching',views.matching,name='matching'),
    path('send_email',views.send_email,name='send_email'),
]