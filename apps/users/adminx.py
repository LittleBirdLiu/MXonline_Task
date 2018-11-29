# _*_ encoding: utf-8 _*_

__author__ = 'Allen'
import xadmin
from xadmin import views
from .models import EmailVerifyRecord, Banner


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = '暮学后台管理系统'
    site_footer = '暮学后台'
    menu_style = 'accordion'


class EmailVerifyRecordAdmin(object):
    # code = models.CharField(max_length=20, verbose_name='验证码')
    # email = models.EmailField(max_length=50, verbose_name='邮箱')
    # send_type = models.CharField(choices=(('register', '注册'), ('forget', u'忘记密码')), max_length=20, verbose_name='发送类型')
    # send_time = models.DateTimeField(default=datetime.now, verbose_name='发送时间')

    list_display = ['code', 'email', 'send_type', 'send_time']
    search_fields = ['code', 'email', 'send_type']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    search_fields = ['title', 'image', 'url', 'index']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
