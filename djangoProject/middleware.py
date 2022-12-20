from utils.token import check_token
from django.http import JsonResponse

try:
    from django.utils.deprecation import MiddlewareMixin
except ImportError:
    MiddlewareMixin = object

# 白名单，表示请求里面的路由时不验证登录信息
API_WHITELIST = ["/users/login", "/users/register"]


class AuthorizeMiddleware(MiddlewareMixin):
    @staticmethod
    def process_request(request):
        if request.path not in API_WHITELIST:
            # 从请求头中获取 username 和 token
            email = request.META.get('HTTP_EMAIL')
            token = request.META.get('HTTP_AUTHORIZATION')
            if email is None or token is None:
                return JsonResponse({'errno': 100001, 'msg': "未查询到登录信息"})
            else:
                # 调用 check_token 函数验证
                if check_token(email, token):
                    pass
                else:
                    return JsonResponse({'errno': 100002,
                                         'msg': "登录信息错误或已过期"})
