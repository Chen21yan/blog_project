from django import forms
from django.contrib.auth import get_user_model
from .models import CaptchaModel

# 表单的作用
# Django 表单可以自动生成 HTML <form> 及其字段（如 <input>、<select>、<textarea> 等），减少手动编写 HTML 的工作量。
# Django 表单会自动验证用户提交的数据是否符合要求（如必填字段、邮箱格式、最小/最大长度等）。
# Django 表单默认包含 {% csrf_token %}，防止跨站请求伪造（CSRF）攻击。
# 表单可以对数据进行额外处理（如去除空格、转换格式等）。
# ModelForm 可以直接关联 Django 模型（Model），自动生成表单字段并保存数据到数据库。

User = get_user_model()

class RegisterForm(forms.Form):
    username = forms.CharField(max_length=20, min_length=2, error_messages={
        'required': '请传入用户名！',
        "max_length":'用户名长度在2~20之间！',
        "min_length": '用户名长度在2~20之间！'
    })
    email = forms.EmailField(error_messages={"required": '请传入邮箱！', 'invalid': '请传入一个正确的邮箱！'})
    captcha = forms.CharField(max_length=4, min_length=4)
    password = forms.CharField(max_length=20, min_length=6)

    def clean_email(self):
        email = self.cleaned_data.get('email')
        exists = User.objects.filter(email=email).exists()
        if exists:
            raise forms.ValidationError('邮箱已经被注册！')
        return email

    def clean_captcha(self):
        captcha = self.cleaned_data.get('captcha')
        email = self.cleaned_data.get('email')

        captcha_model = CaptchaModel.objects.filter(email=email, captcha=captcha).first()
        if not captcha_model:
            raise forms.ValidationError("验证码和邮箱不匹配！")
        captcha_model.delete()
        return captcha


class LoginForm(forms.Form):
    email = forms.EmailField(error_messages={"required": '请传入邮箱！', 'invalid': '请传入一个正确的邮箱！'})
    password = forms.CharField(max_length=20, min_length=6)
    remember = forms.IntegerField(required=False)