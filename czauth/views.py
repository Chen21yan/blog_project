from django.shortcuts import render
from django.http.response import JsonResponse
import string
import random
from django.core.mail import send_mail

# Create your views here.

def login(request):
    return render(request, 'login.html')


def register(request):
    return render(request, 'register.html')


def send_email_captcha(request):
    # ?email=xxx
    email = request.GET.get('email')
    if not email:
        return JsonResponse({'code': 400, 'message': '必须传递邮箱！'})
    # 生成验证码（取随机4位阿拉伯数字）
    # ['0', '2', '9', '4']
    captcha = "".join(random.sample(string.digits, 4))
    send_mail("橙子博客注册验证码", message=f"您的注册验证码是:{captcha}", recipient_list=[email], from_email=None)
    return JsonResponse({'code': 200, 'message': '邮箱验证码发送成功！'})