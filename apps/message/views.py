from django.shortcuts import render
from django.http import  request
from message.models import UserMessgae
# Create your views here.

def getform(request):
    allmessage = UserMessgae.objects.all()

    for message in allmessage :
        print(message.name)
    message = allmessage[0]

    user_message = UserMessgae()
    # user_message.name = 'No 2'
    # user_message.message='this is 2'
    # user_message.address='shanghai'
    # user_message.object_id = '2'
    # user_message.email = 'shanghai@163.com'
    # user_message.save()

    if request.method=='GET':
        user_message = allmessage[1]

    if request.method == "POST":

        user_message.name = request.POST.get('name','')
        user_message.message = request.POST.get('message','')
        user_message.email= request.POST.get('email','')
        user_message.address=request.POST.get('address','')
        user_message.object_id=request.POST.get('object_id','NO4')
        user_message.save()

    return  render(request,'message_form.html',{'my_message':user_message})

