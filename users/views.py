import json
import re
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

from companies.models import Company
from people.models import Resume
from users.models import *
from utils.hash import hash_code
from utils.token import create_token


# Create your views here.

def get_user(request):
    email = json.loads(request.body)['email']
    try:
        user = User.objects.get(email=email)
    except:
        raise Exception({'status_code': 2, 'message': '邮箱不存在!'})
    return user
    # raise Exception({'status_code': 1, 'message': '没有权限!'})


@csrf_exempt
def register(request):
    if request.method == 'POST':
        email = json.loads(request.body)['email']
        password1 = json.loads(request.body)['password1']
        password2 = json.loads(request.body)['password2']
        is_company = json.loads(request.body)['is_company']

        if User.objects.filter(email=email):
            return JsonResponse({'status_code': 1, 'message': '该邮箱已被注册!'})

        if not re.match('^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{8,18}$', password1):
            return JsonResponse({'status_code': 2, 'message': '密码不符合规范!'})

        if password1 != password2:
            return JsonResponse({'status_code': 3, 'message': '两次输入密码不一致!'})

        new_user = User()
        new_user.email = email
        new_user.password = hash_code(password1)
        new_user.is_company = is_company
        new_user.save()

        if is_company:
            new_company = Company()
            new_company.email = email
            new_company.save()
        else:
            new_resume = Resume()
            new_resume.email = email
            new_resume.save()

        return JsonResponse({'status_code': 0, 'message': '注册成功!'})
    return JsonResponse({'status_code': -1, 'message': '请求方式错误!'})


@csrf_exempt
def login(request):
    if request.method == 'POST':
        email = json.loads(request.body)['email']
        password = json.loads(request.body)['password']
        try:
            user = User.objects.get(email=email)
        except:
            return JsonResponse({'status_code': 1, 'message': '未查询到此用户!'})

        if user.password == hash_code(password):
            token = create_token(email)
            return JsonResponse({'status_code': 0, 'email': email, 'token': token, 'message': '登录成功!'})
        else:
            return JsonResponse({'status_code': 2, 'message': '密码错误!'})
    return JsonResponse({'status_code': -1, 'message': '请求方式错误!'})


@csrf_exempt
def username(request):
    try:
        user = get_user(request)
    except Exception as e:
        return e
    if request.method == 'POST':
        new_val = json.loads(request.body)['username']
        user.username = new_val
        user.save()
        return JsonResponse({'status_code': 0, 'message': '修改成功!'})
    elif request.method == 'GET':
        return JsonResponse({'status_code': 0, 'username': user.username})
    return JsonResponse({'status_code': -1, 'message': '请求方式错误!'})


@csrf_exempt
def password(request):
    if request.method == 'POST':
        try:
            user = get_user(request)
        except Exception as e:
            return e
        old = json.loads(request.body)['password_old']
        new1 = json.loads(request.body)['password_new1']
        new2 = json.loads(request.body)['password_new2']

        if user.password != hash_code(old):
            return JsonResponse({'status_code': 2, 'message': '密码错误!'})

        if new1 != new2:
            return JsonResponse({'status_code': 3, 'message': '两次输入密码不一致!'})
        user.password = hash_code(new1)
        user.save()
        return JsonResponse({'status_code': 0, 'message': '修改成功!'})
    return JsonResponse({'status_code': -1, 'message': '请求方式错误!'})
