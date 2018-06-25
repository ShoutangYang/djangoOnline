# -*- coding:utf-8 -*-
__author__ = 'Tony.Yang'


# 分发 url,include

from django.conf.urls import  url,include
from .views import OrgView,AddUserAskView,OrgHomeView
app_name = 'org'
urlpatterns =[
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    url(r'^add_ask/$',AddUserAskView.as_view(),name='add_ask'),
    url('^home/(?P<org_id>\d+)/$',OrgHomeView.as_view(),name='org_home'),
]
