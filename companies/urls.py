from django.urls import path
from .views import *

urlpatterns = [
    path('upd_corporation_name', upd_corporation_name),
    path('get_corporation_name', get_corporation_name),
    path('upd_corporation_state_of_finance', upd_corporation_state_of_finance),
    path('get_corporation_state_of_finance', get_corporation_state_of_finance),
    path('upd_corporation_introduction', upd_corporation_introduction),
    path('get_corporation_introduction', get_corporation_introduction),
    path('add_corporation_talent_development_list', add_corporation_talent_development_list),
    path('get_corporation_talent_development_list', get_corporation_talent_development_list),
    path('del_corporation_talent_development_list', del_corporation_talent_development_list),
    path('upd_corporation_talent_development', upd_corporation_talent_development),
    path('get_corporation_talent_development', get_corporation_talent_development),
    path('upd_corporation_LRP', upd_corporation_LRP),
    path('get_corporation_LRP', get_corporation_LRP),
    path('upd_corporation_am_time', upd_corporation_am_time),
    path('get_corporation_am_time', get_corporation_am_time),
    path('add_welfare_list', add_welfare_list),
    path('get_welfare_list', get_welfare_list),
    path('del_welfare_list', del_welfare_list),
    path('upd_welfare', upd_welfare),
    path('get_welfare', get_welfare),
    path('add_recruiter_list', add_recruiter_list),
    path('get_recruiter_list', get_recruiter_list),
    path('del_recruiter_list', del_recruiter_list),
    path('upd_recruiter', upd_recruiter),
    path('get_recruiter', get_recruiter),
    path('get_recruiter_job_list', get_recruiter_job_list),
    path('get_corporation_job_list', get_corporation_job_list),
    path('add_job', add_job),
    path('del_job', del_job),
    path('upd_job', upd_job),
    path('get_job', get_job),
    path('search_job', search_job),
    path('search_job_by_name', search_job_by_name),
]
