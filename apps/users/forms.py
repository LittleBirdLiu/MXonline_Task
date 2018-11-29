# _*_ coding: utf-8 _*_
from django import forms

# todo 还不能在网页上显示error 信息, 目前在6-5
class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=5)
