# _*_ coding: utf-8 _*_

from django import forms
from operation.models import UserAsk
import re

class UserAskForm(forms.ModelForm):
    class Meta:
        model = UserAsk
        fields = ['name', 'mobile', 'course_name']

    def clean_mobile(self):
        mobile = self.cleaned_data['mobile']
        regax_mobile = '^(13[0-9]|14[579]|15[0-3,5-9]|16[6]|17[0135678]|18[0-9]|19[89])\\d{8}$'
        p = re.compile(regax_mobile)
        if p.match(mobile):
            return mobile
        else:
            raise forms.ValidationError("手机号码非法", code='mobile invalid')