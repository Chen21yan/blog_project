from django.shortcuts import render
from django.urls.base import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')

def blog_detail(request, blog_id):
    return render(request, 'blog_detail.html')

# 装饰器，用于限制只有已登录用户才能访问pub_blog视图函数。如果用户未登录，则会被重定向到指定
# @login_required(login_url=reverse_lazy("czauth:login"))  #
# @login_required(login_url="/auth/login")

# 需要在settings配置LOGIN_URL = '/auth/login'
@login_required()
def pub_blog(request):
    return render(request, 'pub_blog.html')