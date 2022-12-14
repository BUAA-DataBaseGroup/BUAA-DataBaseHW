from django.urls import path
from .views import *

urlpatterns = [
    path('company_info', company_info),
    path('job_list', job_list),
    path('job_info', job_info),
]
