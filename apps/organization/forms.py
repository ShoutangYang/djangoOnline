# -*- coding:utf-8 -*-
__author__ = 'Tony.Yang'

from    django import forms
import re

from operation.models import UserAsk

# class UserAskForm(forms.Form):
#     name = forms.CharField(required=True,min_length=2,max_length=20)
#     phone = forms.CharField(required=True,min_length=11,max_length=11)
#     course_name = forms.CharField(required=True,min_length=5,max_length=50)

class UserAskForm(forms.ModelForm):
    class Meta:
        model= UserAsk
        fields=['name','mobile','course_name']

    def clean_mobile(self):
        mobile=self.cleaned_data['mobile']
        REGEX_MOBILE = "^1[358]\d{9}$|^147\d{8}$|^176\d{8}$"
        p = re.compile(REGEX_MOBILE)
        if p.match(mobile):
            return mobile
        else:
            raise  forms.ValidationError('手机号码非法',code='mobile_error')
