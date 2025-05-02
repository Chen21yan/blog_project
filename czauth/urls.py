from django.urls import path
from . import views

app_name = 'czauth'

urlpatterns = [
    path('login', views.czlogin, name='login'),
    path('logout', views.czlogout, name='logout'),
    path('register', views.register, name='register'),
    path('captcha', views.send_email_captcha, name='email_captcha'),
]