"""djangoOnline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
import xadmin
from django.conf.urls import  url,include
from message.views import getform
from django.views.static import serve

from users.views import user_login
from users.views import LoginView,RegisterView,ActiveUserView,ForgetPwdView,ResetView,ModifyPwdView
from organization.views import OrgView

from django.views.generic import  TemplateView
from djangoOnline.settings import MEDIA_ROOT
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^form/$',getform,name='form_new'),
    url(r'xadmin/',xadmin.site.urls),
    url(r"^$",TemplateView.as_view(template_name='index.html'),name='index'),
    # path('',TemplateView.as_view(template_name='index.html'),name='index'),
    # url('login/$',user_login,name='login'),# 方法登陆，后台调用 user_login 函数
    url('^login/',LoginView.as_view(),name='login'),# 推荐使用类的方式编写 view
    url('^register/',RegisterView.as_view(),name='register'),
    url('^captcha/',include('captcha.urls')), # 验证码需要在url 添加此usl
    url('^active/(?P<active_code>.*)/$',ActiveUserView.as_view(),name ='user_active'),
    #
    url('forget/',ForgetPwdView.as_view(),name = 'forget_pwd'),
    url('reset/(?P<active_code>.*)/',ResetView.as_view(),name = 'reset_pwd'),
    #
    # # 修改密码url; 用于passwordreset页面提交表单
    path('modify_pwd/', ModifyPwdView.as_view(), name="modify_pwd"),
    # 课程结构首页
    # url(r'org_list/',OrgView.as_view(),name='org_list'),
    # url 分发

    url('^org/',include('organization.urls',namespace='org')),

    url(r'^media/(?P<path>.*)$',serve,{"document_root":MEDIA_ROOT}),
    # 注册url
 # path("register/", RegisterView.as_view(), name = "register" ),


]
