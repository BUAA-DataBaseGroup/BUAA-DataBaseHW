from django.urls import path
from .views import *


urlpatterns = [
    path('my_name', my_name),
    path('my_status', my_status),
    path('my_sex_is_male', my_sex_is_male),
    path('my_birth', my_birth),
    path('my_tel', my_tel),
    path('my_date_of_first_work', my_date_of_first_work),
    path('my_wechat', my_wechat),
    path('my_email', my_email),
    path('my_education', my_education),
    path('my_advantage', my_advantage),

    path('my_expect_work_type', my_expect_work_type),
    path('my_expect_work_place', my_expect_work_place),
    path('my_expect_work_position', my_expect_work_position),
    path('my_expect_work_field', my_expect_work_field),
    path('my_expect_salary', my_expect_salary),

    path('my_work_list', my_work_list),
    path('company_name', company_name),
    path('company_field', company_field),
    path('company_department', company_department),
    path('company_position', company_position),
    path('company_start', company_start),
    path('company_end', company_end),
    path('company_content', company_content),
    path('company_achievement', company_achievement),

    path('my_item_list', my_item_list),
    path('item_name', item_name),
    path('item_role', item_role),
    path('item_link', item_link),
    path('item_start', item_start),
    path('item_end', item_end),
    path('item_description', item_description),
    path('item_achievement', item_achievement),

    path('my_education_list', my_education_list),

    path('education_name', education_name),
    path('education_record', education_record),
    path('education_subject', education_subject),
    path('education_start', education_start),
    path('education_end', education_end),
    path('education_experience', education_experience),
]
