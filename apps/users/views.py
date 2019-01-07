# _*_ encoding:utf-8 _*_

from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q
from .models import UserProfile,EmailVerifyRecord
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from .forms import LoginForm, ReigsterForm, ForgetForm, ResetPasswordForm
from utils.send_mail import send_register_mail

class custom_backend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            print('login OK')
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            print(user_name, pass_word)
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                print(user)
                if user.is_active:
                    login(request, user)
                    return render(request, 'index.html')
                else:
                    return render(request, "login.html", {"msg": u"用户未激活"})
            else:
                return render(request, "login.html", {"msg": u"用户名或者密码错误"})
        else:
            print(login_form.errors)
            return render(request, "login.html", {"login_form": login_form})


class RegisterView(View):
    def get(self, request):
        register_form = ReigsterForm()
        return render(request, "register.html", {'register_form': register_form})

    def post(self, request):
        register_form = ReigsterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email', '')
            pass_word = request.POST.get('password', '')
            user_profile = UserProfile()
            user_profile.username = user_name
            user_profile.email = user_name
            if UserProfile.objects.filter(email=user_name):
                return render(request, "register.html", {'msg': u"用户已经存在", 'register_form': register_form})
            user_profile.password = make_password(pass_word)
            user_profile.is_active = False
            user_profile.save()
            send_status = send_register_mail(user_name, 'register')
            if send_status:
                print('send mail ok!, register OK! ')
                return render(request, "login.html")
            else:
                return render(request, "register.html", {'register_form': register_form})

        else:
            return render(request, "register.html", {'register_form': register_form})


class ActiveView(View):
    def get(self, request, active_code):
        print('active code is ', active_code)
        all_code = EmailVerifyRecord.objects.filter(code=active_code)
        if all_code:
            for record in all_code:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
        else:
            return render(request, 'active_fail.html')
        return render(request, 'login.html')


class ForgetView(View):
    def get(self, request):
        return render(request, 'forgetpwd.html', {'forget_form' : ForgetForm})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email', '')
            send_status = send_register_mail(email=email, send_type='forget')
            if send_status:
                return render(request, 'send_success.html')
        else:
            return render(request, 'forgetpwd.html', {'forget_form': forget_form})


class ResetView(View):
    def get(self, request, active_code):
        print('active code is ', active_code)
        all_code = EmailVerifyRecord.objects.filter(code=active_code)
        if all_code:
            for record in all_code:
                email = record.email
                return render(request, 'password_reset.html', {'email': email})
        else:
            return render(request, 'active_fail.html')
        return render(request, 'login.html')


class ModifyView(View):
    def post(self, request):
        reset_pwd_form = ResetPasswordForm(request.POST)
        if reset_pwd_form.is_valid():
            new_pwd = request.POST.get('new_pwd', '')
            confirmed_pwd = request.POST.get('confirmed_pwd', '')
            email = request.POST.get('email', '')
            if new_pwd != confirmed_pwd:
                return render(request, 'password_reset.html', {'email': email, 'msg': u'密码输入不匹配'})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(new_pwd)
            user.save()
            return  render(request, 'login.html')