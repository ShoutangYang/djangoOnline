# -*- coding:utf-8 -*-
__author__ = 'Tony.Yang'

from    django import forms

from operation.models import UserAsk

# class UserAskForm(forms.Form):
#     name = forms.CharField(required=True,min_length=2,max_length=20)
#     phone = forms.CharField(required=True,min_length=11,max_length=11)
#     course_name = forms.CharField(required=True,min_length=5,max_length=50)

class AntherUserForm(forms.ModelForm):
    class Meta:
        model= UserAsk
        fileds=['name','mobile','course_name']