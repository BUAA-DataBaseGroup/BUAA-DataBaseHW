import json

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
        raise Exception(JsonResponse({'status_code': 2, 'message': '邮箱不存在!'}))
    return user
    # raise Exception({'status_code': 1, 'message': '没有权限!'})


def get_company(request):
    email = json.loads(request.body)['email']
    try:
        company = Company.objects.get(email=email)
    except:
        raise Exception(JsonResponse({'status_code': 2, 'message': '公司不存在!'}))
    return company


def get_job_id(request):
    company = get_company(request)
    job_id = json.loads(request.body)['id']
    try:
        job = company.job_set.get(job_id=job_id)
    except:
        raise Exception(JsonResponse({'status_code': 2, 'message': '工作不存在!'}))
    return job


def get_development_id(request):
    company = get_company(request)
    development_id = json.loads(request.body)['id']
    try:
        development = company.development_set.get(development_id=development_id)
    except:
        raise Exception(JsonResponse({'status_code': 2, 'message': 'development不存在!'}))
    return development


def get_welfare_id(request):
    company = get_company(request)
    welfare_id = json.loads(request.body)['id']
    try:
        welfare = company.welfare_set.get(welfare_id=welfare_id)
    except:
        raise Exception(JsonResponse({'status_code': 2, 'message': 'welfare不存在!'}))
    return welfare


def get_recruiter_id(request):
    company = get_company(request)
    recruiter_id = json.loads(request.body)['id']
    try:
        recruiter = company.recruiter_set.get(recruiter_id=recruiter_id)
    except:
        raise Exception(JsonResponse({'status_code': 2, 'message': 'recruiter不存在!'}))
    return recruiter


@csrf_exempt
def upd_corporation_name(request):
    try:
        company = get_company(request)
    except Exception as e:
        return e
    company.corporation_name = json.loads(request.body)['corporation_name']
    company.corporation_abbreviation = json.loads(request.body)['corporation_abbreviation']
    company.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_corporation_name(request):
    try:
        company = get_company(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0,
                         'corporation_name': company.corporation_name,
                         'corporation_abbreviation': company.corporation_abbreviation,
                         })


@csrf_exempt
def upd_corporation_state_of_finance(request):
    try:
        company = get_company(request)
    except Exception as e:
        return e
    company.corporation_state_of_finance = json.loads(request.body)['corporation_state_of_finance']
    company.corporation_size_of_staff = json.loads(request.body)['corporation_size_of_staff']
    company.corporation_field = json.loads(request.body)['corporation_field']
    company.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_corporation_state_of_finance(request):
    try:
        company = get_company(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0,
                         'corporation_state_of_finance': company.corporation_state_of_finance,
                         'corporation_size_of_staff': company.corporation_size_of_staff,
                         'corporation_field': company.corporation_field,
                         })


@csrf_exempt
def upd_corporation_introduction(request):
    try:
        company = get_company(request)
    except Exception as e:
        return e
    company.corporation_introduction = json.loads(request.body)['corporation_introduction']
    company.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_corporation_introduction(request):
    try:
        company = get_company(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0,
                         'corporation_introduction': company.corporation_introduction,
                         })


@csrf_exempt
def add_corporation_talent_development_list(request):
    try:
        company = get_company(request)
    except Exception as e:
        return e
    development = Development()
    development.company = company
    development.content = json.loads(request.body)['content']
    development.save()
    return JsonResponse({'status_code': 0, 'message': '添加成功!'})


@csrf_exempt
def get_corporation_talent_development_list(request):
    try:
        company = get_company(request)
    except Exception as e:
        return e
    development_set = company.development_set
    res = []
    for development in development_set:
        res.append(development.id)
    return JsonResponse({'status_code': 0, 'corporation_talent_development_list': res})


@csrf_exempt
def del_corporation_talent_development_list(request):
    try:
        development = get_development_id(request)
    except Exception as e:
        return e
    development.delete()
    return JsonResponse({'status_code': 0, 'message': '删除成功!'})


@csrf_exempt
def upd_corporation_talent_development(request):
    try:
        development = get_development_id(request)
    except Exception as e:
        return e
    development.content = json.loads(request.body)['content']
    development.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_corporation_talent_development(request):
    try:
        development = get_development_id(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0,
                         'content': development.content,
                         })


@csrf_exempt
def upd_corporation_LRP(request):
    try:
        company = get_company(request)
    except Exception as e:
        return e
    company.corporation_LRP = json.loads(request.body)['corporation_LRP']
    company.corporation_setup_time = json.loads(request.body)['corporation_setup_time']
    company.corporation_type = json.loads(request.body)['corporation_type']
    company.corporation_status = json.loads(request.body)['corporation_status']
    company.corporation_capital = json.loads(request.body)['corporation_capital']
    company.corporation_setup_place = json.loads(request.body)['corporation_setup_place']
    company.corporation_SCC = json.loads(request.body)['corporation_SCC']
    company.corporation_management_content = json.loads(request.body)['corporation_management_content']
    company.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_corporation_LRP(request):
    try:
        company = get_company(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0,
                         'corporation_LRP': company.corporation_LRP,
                         'corporation_setup_time': company.corporation_setup_time,
                         'corporation_type': company.corporation_type,
                         'corporation_status': company.corporation_status,
                         'corporation_capital': company.corporation_capital,
                         'corporation_setup_place': company.corporation_setup_place,
                         'corporation_SCC': company.corporation_SCC,
                         'corporation_management_content': company.corporation_management_content,
                         })


@csrf_exempt
def upd_corporation_am_time(request):
    try:
        company = get_company(request)
    except Exception as e:
        return e
    company.corporation_am_time = json.loads(request.body)['corporation_am_time']
    company.corporation_pm_time = json.loads(request.body)['corporation_pm_time']
    company.corporation_off = json.loads(request.body)['corporation_off']
    company.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_corporation_am_time(request):
    try:
        company = get_company(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0,
                         'corporation_am_time': company.corporation_am_time,
                         'corporation_pm_time': company.corporation_pm_time,
                         'corporation_off': company.corporation_off,
                         })


@csrf_exempt
def add_welfare_list(request):
    try:
        company = get_company(request)
    except Exception as e:
        return e
    welfare = Welfare()
    welfare.company = company
    welfare.content = json.loads(request.body)['content']
    welfare.save()
    return JsonResponse({'status_code': 0, 'message': '添加成功!'})


@csrf_exempt
def get_welfare_list(request):
    try:
        company = get_company(request)
    except Exception as e:
        return e
    welfare_set = company.welfare_set
    res = []
    for welfare in welfare_set:
        res.append(welfare.id)
    return JsonResponse({'status_code': 0, 'corporation_welfare_list': res})


@csrf_exempt
def del_welfare_list(request):
    try:
        welfare = get_welfare_id(request)
    except Exception as e:
        return e
    welfare.delete()
    return JsonResponse({'status_code': 0, 'message': '删除成功!'})


@csrf_exempt
@csrf_exempt
def upd_welfare(request):
    try:
        welfare = get_welfare_id(request)
    except Exception as e:
        return e
    welfare.content = json.loads(request.body)['content']
    welfare.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_welfare(request):
    try:
        welfare = get_welfare_id(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0,
                         'content': welfare.content,
                         })


@csrf_exempt
def add_recruiter_list(request):
    try:
        company = get_company(request)
    except Exception as e:
        return e
    recruiter = Recruiter()
    recruiter.company = company
    recruiter.recruiter_name = json.loads(request.body)['recruiter_name']
    recruiter.recruiter_post = json.loads(request.body)['recruiter_post']
    recruiter.save()
    return JsonResponse({'status_code': 0, 'message': '添加成功!'})


@csrf_exempt
def get_recruiter_list(request):
    try:
        company = get_company(request)
    except Exception as e:
        return e
    recruiter_set = company.recruiter_set
    res = []
    for recruiter in recruiter_set:
        res.append(recruiter.id)
    return JsonResponse({'status_code': 0, 'corporation_recruiter_list': res})


@csrf_exempt
def del_recruiter_list(request):
    try:
        recruiter = get_recruiter_id(request)
    except Exception as e:
        return e
    recruiter.delete()
    return JsonResponse({'status_code': 0, 'message': '删除成功!'})


@csrf_exempt
def upd_recruiter(request):
    try:
        recruiter = get_recruiter_id(request)
    except Exception as e:
        return e
    recruiter.recruiter_name = json.loads(request.body)['recruiter_name']
    recruiter.recruiter_post = json.loads(request.body)['recruiter_post']
    recruiter.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_recruiter(request):
    try:
        recruiter = get_recruiter_id(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0,
                         'recruiter_name': recruiter.recruiter_name,
                         'recruiter_post': recruiter.recruiter_post,
                         })


@csrf_exempt
def get_recruiter_job_list(request):
    try:
        recruiter = get_recruiter_id(request)
    except Exception as e:
        return e
    job_set = recruiter.job_set
    res = []
    for job in job_set:
        res.append(job.id)
    return JsonResponse({'status_code': 0, 'recruiter_job_list': res})


@csrf_exempt
def get_corporation_job_list(request):
    try:
        company = get_company(request)
    except Exception as e:
        return e
    job_set = company.job_set
    res = []
    for job in job_set:
        res.append(job.id)
    return JsonResponse({'status_code': 0, 'corporation_job_list': res})


@csrf_exempt
def add_job(request):
    try:
        company = get_company(request)
        recruiter = get_recruiter(request)
    except Exception as e:
        return e
    job = Job()
    job.company = company
    job.recruiter = recruiter
    job.position_name = json.loads(request.body)['position_name']
    job.position_address = json.loads(request.body)['position_address']
    job.position_experience = json.loads(request.body)['position_experience']
    job.position_education = json.loads(request.body)['position_education']
    job.position_salary_from = json.loads(request.body)['position_salary_from']
    job.position_salary_to = json.loads(request.body)['position_salary_to']
    job.position_description = json.loads(request.body)['position_description']

    job_set = company.job_set
    res = []
    for job in job_set:
        res.append(job.id)
    return JsonResponse({'status_code': 0, 'message': '添加成功!'})


@csrf_exempt
def del_job(request):
    try:
        job = get_job_id(request)
    except Exception as e:
        return e
    job.delete()
    return JsonResponse({'status_code': 0, 'message': '删除成功!'})


@csrf_exempt
def upd_job(request):
    try:
        job = get_job_id(request)
    except Exception as e:
        return e
    recruiter_id = json.loads(request.body)['recruiter_id']
    job.recruiter = Recruiter.objects.get(recruiter_id=recruiter_id)
    job.position_name = json.loads(request.body)['position_name']
    job.position_address = json.loads(request.body)['position_address']
    job.position_experience = json.loads(request.body)['position_experience']
    job.position_education = json.loads(request.body)['position_education']
    job.position_salary_from = json.loads(request.body)['position_salary_from']
    job.position_salary_to = json.loads(request.body)['position_salary_to']
    job.position_boss_id = json.loads(request.body)['position_boss_id']
    job.position_description = json.loads(request.body)['position_description']
    job.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_job(request):
    try:
        job = get_job_id(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0,
                         'recruiter_id': job.recruiter_id,
                         'position_name': job.position_name,
                         'position_address': job.position_address,
                         'position_experience': job.position_experience,
                         'position_education': job.position_education,
                         'position_salary_from': job.position_salary_from,
                         'position_salary_to': job.position_salary_to,
                         'position_boss_id': job.position_boss_id,
                         'position_description': job.position_description,
                         })
