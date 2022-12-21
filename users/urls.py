from django.urls import path
from .views import *

urlpatterns = [
    path('login', login),
    path('register', register),
    path('upd_username', upd_username),
    path('get_username', get_username),
    path('upd_password', upd_password),
]
