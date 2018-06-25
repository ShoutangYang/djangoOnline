# -*- coding:utf-8 -*-
__author__ = 'Tony.Yang'


# 分发 url,include

from django.conf.urls import  url,include
from .views import OrgView,AddUserAskView,OrgHomeView,OrgCourseView,OrgDescView,OrgTeachersView
app_name = 'org'
urlpatterns =[
    url(r'^list/$', OrgView.as_view(), name='org_list'),
    url(r'^add_ask/$',AddUserAskView.as_view(),name='add_ask'),
    url('^home/(?P<org_id>\d+)/$',OrgHomeView.as_view(),name='org_home'),
    url('^course/(?P<org_id>\d+)/$',OrgCourseView.as_view(),name='org_course'),
    url('^desc/(?P<org_id>\d+)/$',OrgDescView.as_view(),name='org_desc'),
    url('^teachers/(?P<org_id>\d+)/$',OrgTeachersView.as_view(),name='org_teachers'),
]
