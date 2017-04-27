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

              return render(request, 'createmessage.html', {'messageSent': 1, 'users': users})
        else:
            return render(request, 'createmessage.html', {'messageSent': 0, 'users': users})
    else:
        return render(request, 'base.html', {'notLoggedIn': 1})

def viewMessage(request):

    #current_user=request.user.is_authenticated()
    #messages=Message.objects.all().filter(sender=???)
    messages=Message.objects.all()
    return render(request, 'viewmessages.html', {'messages':messages})

def deleteMessage(request):
    #  sender = request.POST.get('from_name', '')
    #  recipient = request.POST.get('to_name', '')
    #  messagebody = request.POST.get('message_content', '')
    # # deletebutton = request.POST.get('delete', '')

    messages = Message.objects.all()
   #Message(sender=sender, recipient=recipient, messagebody=messagebody, deletebutton)

    if request.method == 'POST':


        checkbox = request.POST.getlist('deletebox')

        for messagebody in checkbox:

            messages.filter(messagebody=messagebody).delete()

        # if message.delete == true:
        #     messages.filter(sender=sender, recipient=recipient, messagebody = messagebody, delete=delete).delete()
            #

            return render(request, 'viewmessages.html', {'messages': messages})


    else:
        return render(request, 'viewmessages.html', {'messages': messages})

