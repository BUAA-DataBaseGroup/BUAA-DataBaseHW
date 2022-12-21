import json
import re
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from users.models import User
from people.models import *


# Create your views here.

def get_user(request):
    email = json.loads(request.body)['email']
    try:
        user = User.objects.get(email=email)
    except:
        raise Exception({'status_code': 2, 'message': '邮箱不存在!'})
    return user
    # raise Exception({'status_code': 1, 'message': '没有权限!'})


def get_resume(request):
    email = json.loads(request.body)['email']
    try:
        resume = Resume.objects.get(email=email)
    except:
        raise Exception({'status_code': 2, 'message': '简历不存在!'})
    return resume


def get_work(request):
    resume = get_resume(request)
    work_id = json.loads(request.body)['id']
    try:
        work = resume.work_set.get(work_id=work_id)
    except:
        raise Exception({'status_code': 2, 'message': '工作不存在!'})
    return work


def get_item(request):
    resume = get_resume(request)
    item_id = json.loads(request.body)['id']
    try:
        item = resume.work_set.get(item_id=item_id)
    except:
        raise Exception({'status_code': 2, 'message': '项目不存在!'})
    return item


def get_education(request):
    resume = get_resume(request)
    education_id = json.loads(request.body)['id']
    try:
        education = resume.work_set.get(education_id=education_id)
    except:
        raise Exception({'status_code': 2, 'message': '教育经历不存在!'})
    return education


@csrf_exempt
def upd_my_name(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['my_name']
    resume.my_name = new_val
    resume.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_my_name(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'my_name': resume.my_name})


@csrf_exempt
def upd_my_status(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['my_status']
    resume.my_status = new_val
    resume.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_my_status(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'my_status': resume.my_status})


@csrf_exempt
def upd_my_sex_is_male(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['my_sex_is_male']
    resume.my_sex_is_male = new_val
    resume.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_my_sex_is_male(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'my_sex_is_male': resume.my_sex_is_male})


@csrf_exempt
def upd_my_birth(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['my_birth']
    resume.my_birth = new_val
    resume.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_my_birth(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'my_birth': resume.my_birth})


@csrf_exempt
def upd_my_tel(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['my_tel']
    if not re.match('^[0-9]{11}$', new_val):
        return JsonResponse({'status_code': 1, 'message': '手机号不符合规范!'})
    else:
        resume.my_tel = new_val
        resume.save()
        return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_my_tel(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'my_tel': resume.my_tel})


@csrf_exempt
def upd_my_date_of_first_work(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['my_date_of_first_work']
    resume.my_date_of_first_work = new_val
    resume.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_my_date_of_first_work(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'my_date_of_first_work': resume.my_date_of_first_work})


@csrf_exempt
def upd_my_wechat(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['my_wechat']
    resume.my_wechat = new_val
    resume.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_my_wechat(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'my_wechat': resume.my_wechat})


@csrf_exempt
def get_my_email(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'my_email': resume.email})


@csrf_exempt
def get_my_education(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    education_set = resume.education_set
    res = -1
    for education in education_set:
        res = max(res, education.education_record)
    return JsonResponse({'status_code': 0, 'my_education': res})


@csrf_exempt
def upd_my_advantage(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['my_advantage']
    resume.my_advantage = new_val
    resume.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_my_advantage(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'my_advantage': resume.my_advantage})


@csrf_exempt
def upd_my_expect_work_type(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['my_expect_work_type']
    resume.my_expect_work_type = new_val
    resume.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_my_expect_work_type(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'my_expect_work_type': resume.my_expect_work_type})


@csrf_exempt
def upd_my_expect_work_place(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['my_expect_work_place']
    resume.my_expect_work_place = new_val
    resume.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_my_expect_work_place(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'my_expect_work_place': resume.my_expect_work_place})


@csrf_exempt
def upd_my_expect_work_position(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['my_expect_work_position']
    resume.my_expect_work_position = new_val
    resume.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_my_expect_work_position(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'my_expect_work_position': resume.my_expect_work_position})


@csrf_exempt
def upd_my_expect_work_field(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['my_expect_work_field']
    resume.my_expect_work_field = new_val
    resume.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_my_expect_work_field(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'my_expect_work_field': resume.my_expect_work_field})


@csrf_exempt
def upd_my_expect_salary(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['my_expect_salary']
    resume.my_expect_salary = new_val
    resume.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_my_expect_salary(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'my_expect_salary': resume.my_expect_salary})


@csrf_exempt
def add_my_work_list(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    new_company_name = json.loads(request.body)['company_name']
    new_company_field = json.loads(request.body)['company_field']
    new_company_department = json.loads(request.body)['company_department']
    new_company_position = json.loads(request.body)['company_position']
    new_company_start = json.loads(request.body)['company_start']
    new_company_end = json.loads(request.body)['company_end']
    new_company_content = json.loads(request.body)['company_content']
    new_company_achievement = json.loads(request.body)['company_achievement']

    new_work = Work()
    new_work.resume = resume
    new_work.company_name = new_company_name
    new_work.company_field = new_company_field
    new_work.company_department = new_company_department
    new_work.company_department = new_company_department
    new_work.company_position = new_company_position
    new_work.company_start = new_company_start
    new_work.company_end = new_company_end
    new_work.company_content = new_company_content
    new_work.company_achievement = new_company_achievement
    new_work.save()
    return JsonResponse({'status_code': 0, 'message': '添加成功!'})


@csrf_exempt
def get_my_work_list(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    work_set = resume.work_set
    res = []
    for work in work_set:
        res.append(work.id)


@csrf_exempt
def del_my_work_list(request):
    try:
        work = get_work(request)
    except Exception as e:
        return e
    work.delete()
    return JsonResponse({'status_code': 0, 'message': '删除成功!'})


@csrf_exempt
def upd_company_name(request):
    try:
        work = get_work(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['company_name']
    work.company_name = new_val
    work.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_company_name(request):
    try:
        work = get_work(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'company_name': work.company_name})


@csrf_exempt
def upd_company_field(request):
    try:
        work = get_work(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['company_field']
    work.company_field = new_val
    work.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_company_field(request):
    try:
        work = get_work(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'company_field': work.company_field})


@csrf_exempt
def upd_company_department(request):
    try:
        work = get_work(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['company_department']
    work.company_department = new_val
    work.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_company_department(request):
    try:
        work = get_work(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'company_department': work.company_department})


@csrf_exempt
def upd_company_position(request):
    try:
        work = get_work(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['company_position']
    work.company_position = new_val
    work.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_company_position(request):
    try:
        work = get_work(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'company_position': work.company_position})


@csrf_exempt
def upd_company_start(request):
    try:
        work = get_work(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['company_start']
    work.company_start = new_val
    work.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_company_start(request):
    try:
        work = get_work(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'company_start': work.company_start})


@csrf_exempt
def upd_company_end(request):
    try:
        work = get_work(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['company_end']
    work.company_end = new_val
    work.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_company_end(request):
    try:
        work = get_work(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'company_end': work.company_end})


@csrf_exempt
def upd_company_content(request):
    try:
        work = get_work(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['company_content']
    work.company_content = new_val
    work.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_company_content(request):
    try:
        work = get_work(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'company_content': work.company_content})


@csrf_exempt
def upd_company_achievement(request):
    try:
        work = get_work(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['company_achievement']
    work.company_achievement = new_val
    work.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_company_achievement(request):
    try:
        work = get_work(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'company_achievement': work.company_achievement})


@csrf_exempt
def add_my_item_list(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    new_item_name = json.loads(request.body)['item_name']
    new_item_role = json.loads(request.body)['item_role']
    new_item_link = json.loads(request.body)['item_link']
    new_item_start = json.loads(request.body)['item_start']
    new_item_end = json.loads(request.body)['item_end']
    new_item_description = json.loads(request.body)['item_description']
    new_item_achievement = json.loads(request.body)['item_achievement']

    new_item = Item()
    new_item.resume = resume
    new_item.item_name = new_item_name
    new_item.item_role = new_item_role
    new_item.item_link = new_item_link
    new_item.item_start = new_item_start
    new_item.item_end = new_item_end
    new_item.item_description = new_item_description
    new_item.item_achievement = new_item_achievement
    new_item.save()
    return JsonResponse({'status_code': 0, 'message': '添加成功!'})


@csrf_exempt
def get_my_item_list(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    item_set = resume.item_set
    res = []
    for item in item_set:
        res.append(item.item_id)
    return JsonResponse({'status_code': 0, 'my_item_list': res})


@csrf_exempt
def del_my_item_list(request):
    try:
        item = get_item(request)
    except Exception as e:
        return e
    item.delete()
    return JsonResponse({'status_code': 0, 'message': '删除成功!'})


@csrf_exempt
def upd_item_name(request):
    try:
        item = get_item(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['item_name']
    item.item_name = new_val
    item.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_item_name(request):
    try:
        item = get_item(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'item_name': item.item_name})


@csrf_exempt
def upd_item_role(request):
    try:
        item = get_item(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['item_role']
    item.item_role = new_val
    item.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_item_role(request):
    try:
        item = get_item(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'item_role': item.item_role})


@csrf_exempt
def upd_item_link(request):
    try:
        item = get_item(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['item_link']
    item.item_link = new_val
    item.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_item_link(request):
    try:
        item = get_item(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'item_link': item.item_link})


@csrf_exempt
def upd_item_start(request):
    try:
        item = get_item(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['item_start']
    item.item_start = new_val
    item.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_item_start(request):
    try:
        item = get_item(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'item_start': item.item_start})


@csrf_exempt
def upd_item_end(request):
    try:
        item = get_item(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['item_end']
    item.item_end = new_val
    item.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_item_end(request):
    try:
        item = get_item(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'item_end': item.item_end})


@csrf_exempt
def upd_item_description(request):
    try:
        item = get_item(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['item_description']
    item.item_description = new_val
    item.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_item_description(request):
    try:
        item = get_item(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'item_description': item.item_description})


@csrf_exempt
def upd_item_achievement(request):
    try:
        item = get_item(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['item_achievement']
    item.item_achievement = new_val
    item.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_item_achievement(request):
    try:
        item = get_item(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'item_achievement': item.item_achievement})


@csrf_exempt
def add_my_education_list(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    new_education_name = json.loads(request.body)['education_name']
    new_education_record = json.loads(request.body)['education_record']
    new_education_subject = json.loads(request.body)['education_subject']
    new_education_start = json.loads(request.body)['education_start']
    new_education_end = json.loads(request.body)['education_end']
    new_education_experience = json.loads(request.body)['education_experience']

    new_education = Education()
    new_education.resume = resume
    new_education.education_name = new_education_name
    new_education.education_record = new_education_record
    new_education.education_subject = new_education_subject
    new_education.education_start = new_education_start
    new_education.education_end = new_education_end
    new_education.education_experience = new_education_experience
    new_education.save()
    return JsonResponse({'status_code': 0, 'message': '添加成功!'})


@csrf_exempt
def get_my_education_list(request):
    try:
        resume = get_resume(request)
    except Exception as e:
        return e
    education_set = resume.education_set
    res = []
    for education in education_set:
        res.append(education.education_id)
    return JsonResponse({'status_code': 0, 'my_education_list': res})


@csrf_exempt
def del_my_education_list(request):
    try:
        education = get_education(request)
    except Exception as e:
        return e
    education.delete()
    return JsonResponse({'status_code': 0, 'message': '删除成功!'})


@csrf_exempt
def upd_education_name(request):
    try:
        education = get_education(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['education_name']
    education.education_name = new_val
    education.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_education_name(request):
    try:
        education = get_education(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'education_name': education.education_name})


@csrf_exempt
def upd_education_record(request):
    try:
        education = get_education(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['education_record']
    education.education_record = new_val
    education.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_education_record(request):
    try:
        education = get_education(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'education_record': education.education_record})


@csrf_exempt
def upd_education_subject(request):
    try:
        education = get_education(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['education_subject']
    education.education_subject = new_val
    education.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_education_subject(request):
    try:
        education = get_education(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'education_subject': education.education_subject})


@csrf_exempt
def upd_education_start(request):
    try:
        education = get_education(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['education_start']
    education.education_start = new_val
    education.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_education_start(request):
    try:
        education = get_education(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'education_start': education.education_start})


@csrf_exempt
def upd_education_end(request):
    try:
        education = get_education(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['education_end']
    education.education_end = new_val
    education.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_education_end(request):
    try:
        education = get_education(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'education_end': education.education_end})


@csrf_exempt
def upd_education_experience(request):
    try:
        education = get_education(request)
    except Exception as e:
        return e
    new_val = json.loads(request.body)['education_experience']
    education.education_experience = new_val
    education.save()
    return JsonResponse({'status_code': 0, 'message': '修改成功!'})


@csrf_exempt
def get_education_experience(request):
    try:
        education = get_education(request)
    except Exception as e:
        return e
    return JsonResponse({'status_code': 0, 'education_experience': education.education_experience})
