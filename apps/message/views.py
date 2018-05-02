from django.shortcuts import render
from django.http import  request
from message.models import UserMessgae
# Create your views here.

def getform(request):
    allmessage = UserMessgae.objects.all()

    for message in allmessage :
        print(message)
    message = allmessage[0]
    return  render(request,'message_form.html',{'my_message':message})

