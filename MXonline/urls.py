#_*_ coding: utf-8 _*_

"""MXonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
import xadmin
from django.views.generic import TemplateView
from users.views import LoginView, RegisterView,ActiveView, ForgetView, ResetView, ModifyView
from organization.views import Org_List_View
from django.views.static import serve
from MXonline.settings import MEDIA_ROOT


urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url('^$', TemplateView.as_view(template_name='index.html'), name='index'),
    url('^login/$', LoginView.as_view(), name='login'),
    url('^register/$', RegisterView.as_view(), name='register'),
    url(r'^captcha/', include('captcha.urls')),
    # if the pattern is (?P<id>[a-zA-Z_]\w*), the group can be referenced by its name in arguments to methods of
    # match objects, such as m.group('id') or m.end('id'), and also by name in the regular expression itself (using (
    # ?P=id)) and replacement text given to .sub() (using \g<id>).
    url(r'^active/(?P<active_code>.*)/$', ActiveView.as_view(), name='active'),
    url(r'^forget/$', ForgetView.as_view(), name='forget'),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name='reset'),
    url(r'^modify_pwd/$', ModifyView.as_view(), name='modify_pwd'),

    # 课程url 配置
    url(r'org/', include('organization.urls', namespace="org")),
    # course URL configuration
    url(r'course/', include('course.urls', namespace='course')),

    url(r'media/(?P<path>.*)', serve, {'document_root': MEDIA_ROOT})


]