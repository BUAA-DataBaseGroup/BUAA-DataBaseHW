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


@csrf_exempt
def register(request):
    if request.method == 'POST':
        username = json.loads(request.body)['username']
        password1 = json.loads(request.body)['password1']
        password2 = json.loads(request.body)['password2']
        email = json.loads(request.body)['email']
        is_company = json.loads(request.body)['is_company']

        if User.objects.filter(username=username):
            return JsonResponse({'status_code': 1, 'message': '用户名已存在!'})

        if User.objects.filter(email=email):
            return JsonResponse({'status_code': 2, 'message': '该邮箱已被注册!'})

        if not re.match('^(?![0-9]+$)(?![a-zA-Z]+$)[0-9A-Za-z]{8,18}$', password1):
            return JsonResponse({'status_code': 3, 'message': '密码不符合规范!'})

        if password1 != password2:
            return JsonResponse({'status_code': 4, 'message': '两次输入密码不一致!'})

        new_user = User()
        new_user.username = username
        new_user.password = hash_code(password1)
        new_user.email = email
        new_user.is_company = is_company
        new_user.save()

        if is_company:
            new_company = Company()
            new_company.username = username
            company_name = json.loads(request.body)['company_name']
            new_company.company_name = company_name
            new_company.save()
        else:
            new_resume = Resume()
            new_resume.username = username
            new_resume.my_email = email
            new_resume.save()

        return JsonResponse({'status_code': 0, 'message': '注册成功!'})
    return JsonResponse({'status_code': -1, 'message': '请求方式错误!'})


@csrf_exempt
def login(request):
    if request.method == 'POST':
        username = json.loads(request.body)['username']
        password = json.loads(request.body)['password']
        try:
            user = User.objects.get(username=username)
        except:
            return JsonResponse({'status_code': 1, 'message': '未查询到此用户!'})

        if user.password == hash_code(password):
            token = create_token(username)
            return JsonResponse({'status_code': 0, 'username': username, 'token': token, 'message': '登录成功!'})
        else:
            return JsonResponse({'status_code': 2, 'message': '密码错误!'})
    return JsonResponse({'status_code': -1, 'message': '请求方式错误!'})