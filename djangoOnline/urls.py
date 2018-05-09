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
from django.urls import path
import xadmin
from django.conf.urls import  url
from message.views import getform
from users.views import user_login


from django.views.generic import  TemplateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^form/$',getform,name='form_new'),
    path('xadmin/',xadmin.site.urls),
    path('',TemplateView.as_view(template_name='index.html'),name='index'),
    path('login/',user_login,name='login'),

    # 注册url
 # path("register/", RegisterView.as_view(), name = "register" )


]
