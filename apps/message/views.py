from django.shortcuts import render
import MySQLdb

from .models import UserMessage


def getform(request):  # Http request object
    # all_messages = UserMessage.objects.filter(name='bobby')
    # for message in all_messages:
    #     print(message.name)
    if request.method == "POST":
        name = request.POST.get('name', '')
        message = request.POST.get('message', '')
        address = request.POST.get('address', '')
        email = request.POST.get('email', '')
        user_message = UserMessage()
        user_message.name = name
        user_message.message = message
        user_message.address = address
        user_message.email = email
        user_message.object_id = 'helloworld3'
        user_message.save()
    return render(request, 'message/form.html')