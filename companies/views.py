import json
import re

from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from users.models import User
from companies.models import *


# Create your views here.

def get_user(request):
    email = json.loads(request.body)['email']
    try:
        user = User.objects.get(email=email)
    except:
        raise Exception({'status_code': 2, 'message': '邮箱不存在!'})
    return user
    # raise Exception({'status_code': 1, 'message': '没有权限!'})


def get_company(request):
    email = json.loads(request.body)['email']
    try:
        company = Company.objects.get(email=email)
    except:
        raise Exception({'status_code': 2, 'message': '公司不存在!'})
    return company


def get_job(request):
    company = get_company(request)
    job_id = json.loads(request.body)['id']
    try:
        job = company.job_set.get(job_id=job_id)
    except:
        raise Exception({'status_code': 2, 'message': '工作不存在!'})
    return job


@csrf_exempt
def company_info(request):
    try:
        company = get_company(request)
    except Exception as e:
        return e
    if request.method == 'POST':
        new_company_name = json.loads(request.body)['company_name']
        new_company_position = json.loads(request.body)['company_position']
        new_company_description = json.loads(request.body)['company_description']
        new_company_tag1 = json.loads(request.body)['company_tag1']
        new_company_tag2 = json.loads(request.body)['company_tag2']
        new_company_tag3 = json.loads(request.body)['company_tag3']

        company.company_name = new_company_name
        company.company_position = new_company_position
        company.company_description = new_company_description
        company.company_tag1 = new_company_tag1
        company.company_tag2 = new_company_tag2
        company.company_tag3 = new_company_tag3
        company.save()
        return JsonResponse({'status_code': 0, 'message': '修改成功!'})
    elif request.method == 'GET':
        return JsonResponse({'status_code': 0,
                             'company_name': company.company_name,
                             'company_position': company.company_position,
                             'company_description': company.company_description,
                             'company_tag1': company.company_tag1,
                             'company_tag2': company.company_tag2,
                             'company_tag3': company.company_tag3,
                             })
    return JsonResponse({'status_code': -1, 'message': '请求方式错误!'})


# @csrf_exempt
# def company_name(request):
#     try:
#         company = get_company(request)
#     except Exception as e:
#         return e
#     if request.method == 'POST':
#         new_val = json.loads(request.body)['company_name']
#         company.company_name = new_val
#         company.save()
#         return JsonResponse({'status_code': 0, 'message': '修改成功!'})
#     elif request.method == 'GET':
#         return JsonResponse({'status_code': 0, 'company_name': company.company_name})
#     return JsonResponse({'status_code': -1, 'message': '请求方式错误!'})
#
#
# @csrf_exempt
# def company_position(request):
#     try:
#         company = get_company(request)
#     except Exception as e:
#         return e
#     if request.method == 'POST':
#         new_val = json.loads(request.body)['company_position']
#         company.company_position = new_val
#         company.save()
#         return JsonResponse({'status_code': 0, 'message': '修改成功!'})
#     elif request.method == 'GET':
#         return JsonResponse({'status_code': 0, 'company_position': company.company_position})
#     return JsonResponse({'status_code': -1, 'message': '请求方式错误!'})
#
#
# @csrf_exempt
# def company_description(request):
#     try:
#         company = get_company(request)
#     except Exception as e:
#         return e
#     if request.method == 'POST':
#         new_val = json.loads(request.body)['company_description']
#         company.company_description = new_val
#         company.save()
#         return JsonResponse({'status_code': 0, 'message': '修改成功!'})
#     elif request.method == 'GET':
#         return JsonResponse({'status_code': 0, 'company_description': company.company_description})
#     return JsonResponse({'status_code': -1, 'message': '请求方式错误!'})
#
#
# @csrf_exempt
# def company_tag1(request):
#     try:
#         company = get_company(request)
#     except Exception as e:
#         return e
#     if request.method == 'POST':
#         new_val = json.loads(request.body)['company_tag1']
#         company.company_tag1 = new_val
#         company.save()
#         return JsonResponse({'status_code': 0, 'message': '修改成功!'})
#     elif request.method == 'GET':
#         return JsonResponse({'status_code': 0, 'company_tag1': company.company_tag1})
#     return JsonResponse({'status_code': -1, 'message': '请求方式错误!'})
#
#
# @csrf_exempt
# def company_tag2(request):
#     try:
#         company = get_company(request)
#     except Exception as e:
#         return e
#     if request.method == 'POST':
#         new_val = json.loads(request.body)['company_tag2']
#         company.company_tag2 = new_val
#         company.save()
#         return JsonResponse({'status_code': 0, 'message': '修改成功!'})
#     elif request.method == 'GET':
#         return JsonResponse({'status_code': 0, 'company_tag2': company.company_tag2})
#     return JsonResponse({'status_code': -1, 'message': '请求方式错误!'})
#
#
# @csrf_exempt
# def company_tag3(request):
#     try:
#         company = get_company(request)
#     except Exception as e:
#         return e
#     if request.method == 'POST':
#         new_val = json.loads(request.body)['company_tag3']
#         company.company_tag3 = new_val
#         company.save()
#         return JsonResponse({'status_code': 0, 'message': '修改成功!'})
#     elif request.method == 'GET':
#         return JsonResponse({'status_code': 0, 'company_tag3': company.company_tag3})
#     return JsonResponse({'status_code': -1, 'message': '请求方式错误!'})

@csrf_exempt
def job_list(request):
    try:
        company = get_company(request)
    except Exception as e:
        return e
    if request.method == 'POST':
        new_job_name = json.loads(request.body)['job_name']
        new_job_salary_min = json.loads(request.body)['job_salary_min']
        new_job_salary_max = json.loads(request.body)['job_salary_max']
        new_job_description = json.loads(request.body)['job_description']
        new_job_day = json.loads(request.body)['job_day']
        new_job_month = json.loads(request.body)['job_month']
        new_job_education = json.loads(request.body)['job_education']

        job = Job()
        job.company = company
        job.job_name = new_job_name
        job.job_salary_min = new_job_salary_min
        job.job_salary_max = new_job_salary_max
        job.job_description = new_job_description
        job.job_day = new_job_day
        job.job_month = new_job_month
        job.job_education = new_job_education
        job.save()
        return JsonResponse({'status_code': 0, 'message': '添加成功!'})
    elif request.method == 'GET':
        job_set = company.job_set
        res = []
        for job in job_set:
            res.append(job.id)
        return JsonResponse({'status_code': 0, 'job_list': res})
    elif request.method == 'DELETE':
        try:
            job = get_job(request)
        except Exception as e:
            return e
        job.delete()
        return JsonResponse({'status_code': 0, 'message': '删除成功!'})
    return JsonResponse({'status_code': -1, 'message': '请求方式错误!'})


@csrf_exempt
def job_info(request):
    try:
        job = get_job(request)
    except Exception as e:
        return e
    if request.method == 'POST':
        new_job_name = json.loads(request.body)['job_name']
        new_job_salary_min = json.loads(request.body)['job_salary_min']
        new_job_salary_max = json.loads(request.body)['job_salary_max']
        new_job_description = json.loads(request.body)['job_description']
        new_job_day = json.loads(request.body)['job_day']
        new_job_month = json.loads(request.body)['job_month']
        new_job_education = json.loads(request.body)['job_education']
        new_contact_name = json.loads(request.body)['contact_name']
        new_contact_tel = json.loads(request.body)['contact_tel']
        new_contact_info = json.loads(request.body)['contact_info']

        if not re.match('^[0-9]{11}$', new_contact_tel):
            return JsonResponse({'status_code': 1, 'message': '手机号不符合规范!'})

        job.job_name = new_job_name
        job.job_salary_min = new_job_salary_min
        job.job_salary_max = new_job_salary_max
        job.job_description = new_job_description
        job.job_day = new_job_day
        job.job_month = new_job_month
        job.job_education = new_job_education
        job.contact_name = new_contact_name
        job.contact_tel = new_contact_tel
        job.contact_info = new_contact_info
        job.save()
        return JsonResponse({'status_code': 0, 'message': '修改成功!'})
    elif request.method == 'GET':
        return JsonResponse({'status_code': 0,
                             'job_name': job.company_name,
                             'job_salary_min': job.company_position,
                             'job_salary_max': job.job_salary_max,
                             'job_description': job.job_description,
                             'job_day': job.job_day,
                             'job_month': job.job_month,
                             'job_education': job.job_education,
                             })
    return JsonResponse({'status_code': -1, 'message': '请求方式错误!'})
