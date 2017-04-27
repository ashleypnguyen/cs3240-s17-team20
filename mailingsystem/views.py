from django.shortcuts import render
from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
#from django.core.context_processors import csrf
from django.template import loader
from django.forms.models import model_to_dict
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from .models import Message
from django.contrib.auth.models import User
from .messageEncrypt import encrypt_val, decrypt_val

# from django.contrib.auth.decorators import login_required

# Create your views here.
#@login_reguired(login_url='/base/')
def sendMessage(request):
    if request.user.username != "":
        messages = Message.objects.all()
        count = 0
        for message in messages:
            if message.recipient == request.user.username:
                count += 1
    if request.user.username != "":
        user_name = request.user
        users = User.objects.all()
        if request.method == 'POST':

              sender = user_name
              recipient = request.POST.get('to_name', '' )
              messagebody = request.POST.get('message_content','')
              encrypt = False
              if request.POST.get('to_encrypt') == 'yes':
                  encrypt = True
              if encrypt:
                  messagebody = encrypt_val(messagebody)

              messageObj=Message(sender=sender, recipient=recipient, messagebody=messagebody, encrypted=encrypt)

              messageObj.save()

              return render(request, 'createmessage.html', {'messageSent': 1, 'users': users, 'num_Messages': count})
        else:
            return render(request, 'createmessage.html', {'messageSent': 0, 'users': users, 'num_Messages': count})
    else:
        return render(request, 'base.html', {'notLoggedIn': 1, 'num_Messages': count})

def viewMessage(request):

    if request.user.username != "":
        messages = Message.objects.all()
        count = 0
        for message in messages:
            if message.recipient == request.user.username:
                count += 1
    messages=Message.objects.all()
    return render(request, 'viewmessages.html', {'messages':messages, 'num_Messages': count})

def deleteMessage(request):

    messages = Message.objects.all()

    if request.method == 'POST':

        checkbox = request.POST.getlist('deletebox')
        count = 0
        for messagebody in checkbox:
            messages.filter(messagebody=messagebody).delete()

        for message in messages:
            if message.recipient == request.user.username:
                count += 1
        return render(request, 'viewmessages.html', {'messages': messages, 'num_Messages': count})


    else:
        return render(request, 'viewmessages.html', {'messages': messages})

