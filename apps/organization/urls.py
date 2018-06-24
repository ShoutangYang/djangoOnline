# -*- coding:utf-8 -*-
__author__ = 'Tony.Yang'


# 分发 url,include

from django.conf.urls import  url,include
from .views import OrgView
app_name = 'org'
urlpatterns =[
    url(r'^list/$', OrgView.as_view(), name='org_list'),

]
