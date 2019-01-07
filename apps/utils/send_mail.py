# _*_ coding: utf-8 _*_
from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from MXonline.settings import EMAIL_FROM

def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz123456789'
    length = len(chars)-1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


def send_register_mail(email, send_type="register"):
    email_record = EmailVerifyRecord()
    code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()
    # email_title = ""
    # email_body = ""

    if send_type == "register":
        email_title = u'email confirm'
        email_body = u'please click the url http://127.0.0.1:8000/active/{0}/'.format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        return send_status

    if send_type == 'forget':
        email_title = u'forget email find'
        email_body = u'please click the url http://127.0.0.1:8000/reset/{0}/'.format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        return send_status


