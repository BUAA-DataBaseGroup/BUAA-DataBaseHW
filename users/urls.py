from django.urls import path
from .views import *

urlpatterns = [
    path('login', login),
    path('register', register),
    path('username', username),
    path('password', password),
]
