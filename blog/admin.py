from django.contrib import admin
from .models import Blog, BlogComment, BlogCategory

# 将 Django 模型（Blog、BlogComment、BlogCategory）注册到 Django Admin 后台管理界面，并自定义它们的显示方式。

# BlogCategoryAdmin：控制 BlogCategory 在 Admin 后台的显示方式。
class BlogCategoryAdmin(admin.ModelAdmin):
    # 在列表页只显示 `name` 字段
    list_display = ['name']

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'pub_time', 'category', 'author']

class BlogCommentAdmin(admin.ModelAdmin):
    list_display = ['content', 'pub_time', 'author', 'blog']


# 模型注册到admin后台
admin.site.register(Blog, BlogAdmin)
admin.site.register(BlogComment, BlogCommentAdmin)
admin.site.register(BlogCategory, BlogCategoryAdmin)