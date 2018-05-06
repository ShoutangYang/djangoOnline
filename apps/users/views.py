from django.shortcuts import render
from django.views import  View
from django.http import  request
# Create your views here.
def login(request):
    if request.method =='POST':
        pass
    elif request.method=='GET':
        return  render(request,'login.html',{})

class   RegisterView(View):
    def get (self,request):
        return render(request,'register.html')