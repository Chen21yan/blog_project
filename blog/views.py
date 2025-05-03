from django.shortcuts import render, redirect, reverse
from django.http.response import JsonResponse
from django.urls.base import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods, require_POST
from .models import BlogCategory, Blog, BlogComment
from .forms import PubBlogForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

def blog_detail(request, blog_id):
    try:
        blog = Blog.objects.get(pk=blog_id)
    except Exception as e:
        blog = None
    return render(request, 'blog_detail.html', context={'blog': blog})

# 装饰器，用于限制只有已登录用户才能访问pub_blog视图函数。如果用户未登录，则会被重定向到指定
# @login_required(login_url=reverse_lazy("czauth:login"))  #
# @login_required(login_url="/auth/login")

# 需要在settings配置LOGIN_URL = '/auth/login'
@require_http_methods(['GET', 'POST'])
@login_required()
def pub_blog(request):
    if request.method == 'GET':
        categories = BlogCategory.objects.all()
        return render(request, 'pub_blog.html', context={"categories": categories})
    else:
        form = PubBlogForm(request.POST)
        if form.is_valid():
            title = form.cleaned_data.get('title')
            content = form.cleaned_data.get('content')
            category_id = form.cleaned_data.get('category')
            blog = Blog.objects.create(title=title, content=content, category_id=category_id, author=request.user)
            return JsonResponse({"code": 200, "message": "博客发布成功！", "data": {"blog_id": blog.id}})
        else:
            print("提交的 POST 数据:", request.POST)
            print("content 值:", request.POST.get('content'))
            print("表单错误:", form.errors)
            return JsonResponse({"code": 400, "message": "参数错误！"})


@require_POST
@login_required()
def pub_comment(request):
    blog_id = request.POST.get('blog_id')
    content = request.POST.get('content')
    BlogComment.objects.create(content=content, blog_id=blog_id, author=request.user)
    # 重新加载博客详情页
    return redirect(reverse("blog:blog_detail", kwargs={'blog_id': blog_id}))
