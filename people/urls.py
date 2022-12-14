from django.urls import path
from .views import *

urlpatterns = [
    path('upd_my_name', upd_my_name),
    path('get_my_name', get_my_name),
    path('upd_my_status', upd_my_status),
    path('get_my_status', get_my_status),
    path('upd_my_sex_is_male', upd_my_sex_is_male),
    path('get_my_sex_is_male', get_my_sex_is_male),
    path('upd_my_birth', upd_my_birth),
    path('get_my_birth', get_my_birth),
    path('upd_my_tel', upd_my_tel),
    path('get_my_tel', get_my_tel),
    path('upd_my_date_of_first_work', upd_my_date_of_first_work),
    path('get_my_date_of_first_work', get_my_date_of_first_work),
    path('upd_my_wechat', upd_my_wechat),
    path('get_my_wechat', get_my_wechat),
    path('get_my_email', get_my_email),
    path('get_my_education', get_my_education),
    path('upd_my_advantage', upd_my_advantage),
    path('get_my_advantage', get_my_advantage),

    path('upd_my_expect_work_type', upd_my_expect_work_type),
    path('get_my_expect_work_type', get_my_expect_work_type),
    path('upd_my_expect_work_place', upd_my_expect_work_place),
    path('get_my_expect_work_place', get_my_expect_work_place),
    path('upd_my_expect_work_position', upd_my_expect_work_position),
    path('get_my_expect_work_position', get_my_expect_work_position),
    path('upd_my_expect_work_field', upd_my_expect_work_field),
    path('get_my_expect_work_field', get_my_expect_work_field),
    path('upd_my_expect_salary', upd_my_expect_salary),
    path('get_my_expect_salary', get_my_expect_salary),

    path('add_my_work_list', add_my_work_list),
    path('get_my_work_list', get_my_work_list),
    path('del_my_work_list', del_my_work_list),

    path('upd_company_name', upd_company_name),
    path('get_company_name', get_company_name),
    path('upd_company_field', upd_company_field),
    path('get_company_field', get_company_field),
    path('upd_company_department', upd_company_department),
    path('get_company_department', get_company_department),
    path('upd_company_position', upd_company_position),
    path('get_company_position', get_company_position),
    path('upd_company_start', upd_company_start),
    path('get_company_start', get_company_start),
    path('upd_company_end', upd_company_end),
    path('get_company_end', get_company_end),
    path('upd_company_content', upd_company_content),
    path('get_company_content', get_company_content),
    path('upd_company_achievement', upd_company_achievement),
    path('get_company_achievement', get_company_achievement),

    path('add_my_item_list', add_my_item_list),
    path('get_my_item_list', get_my_item_list),
    path('del_my_item_list', del_my_item_list),

    path('upd_item_name', upd_item_name),
    path('get_item_name', get_item_name),
    path('upd_item_role', upd_item_role),
    path('get_item_role', get_item_role),
    path('upd_item_link', upd_item_link),
    path('get_item_link', get_item_link),
    path('upd_item_start', upd_item_start),
    path('get_item_start', get_item_start),
    path('upd_item_end', upd_item_end),
    path('get_item_end', get_item_end),
    path('upd_item_description', upd_item_description),
    path('get_item_description', get_item_description),
    path('upd_item_achievement', upd_item_achievement),
    path('get_item_achievement', get_item_achievement),

    path('add_my_education_list', add_my_education_list),
    path('get_my_education_list', get_my_education_list),
    path('del_my_education_list', del_my_education_list),

    path('upd_education_name', upd_education_name),
    path('get_education_name', get_education_name),
    path('upd_education_record', upd_education_record),
    path('get_education_record', get_education_record),
    path('upd_education_subject', upd_education_subject),
    path('get_education_subject', get_education_subject),
    path('upd_education_start', upd_education_start),
    path('get_education_start', get_education_start),
    path('upd_education_end', upd_education_end),
    path('get_education_end', get_education_end),
    path('upd_education_experience', upd_education_experience),
    path('get_education_experience', get_education_experience),
]
