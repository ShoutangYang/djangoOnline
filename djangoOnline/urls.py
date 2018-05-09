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
from users.views import user_login
from users.views import LoginView,RegisterView,ActiveUserView

from django.views.generic import  TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^form/$',getform,name='form_new'),
    path('xadmin/',xadmin.site.urls),
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('login/',LoginView.as_view(),name='login'),
    path('register/',RegisterView.as_view(),name='register'),
    path('captcha/',include('captcha.urls')),
    re_path('active/(?P<active_code>.*)/',ActiveUserView.as_view(),name ='user_active'),

    # 注册url
 # path("register/", RegisterView.as_view(), name = "register" )


]
