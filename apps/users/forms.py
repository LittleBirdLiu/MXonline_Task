# _*_ coding: utf-8 _*_
from django import forms
from captcha.fields import CaptchaField
from utils.send_mail import send_register_mail

class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)


class ReigsterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=5)
    captcha = CaptchaField(error_messages={"invalid": u'验证码错误！'})


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField(error_messages={"invalid": u'验证码错误！'})


class ResetPasswordForm(forms.Form):
    new_pwd = forms.CharField(required=True, min_length=5)
    confirmed_pwd = forms.CharField(required=True, min_length=5)
