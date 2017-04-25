from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
#from django.core.context_processors import csrf
from django.template import loader
from .forms import ReportForm
from .models import User, Group
from .models import Report
#from .models import Group
from .forms import UserForm, UserProfileForm, createGroupForm
from django.forms.models import model_to_dict
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse

# Create your views here.
def viewUser(request, user_id):
    if User.objects.filter(id = user_id):
        theUser = User.objects.get(pk = user_id)
    else:
        return HttpResponse("User ID not found")
    # Displaying the user
    if(request.method == "GET"):
        if User.objects.filter(id=user_id):
            user_dict = model_to_dict(theUser)
            return JsonResponse({'status': True, 'resp': user_dict})

# def userSignup(request):
#     form = UserForm()
#     is_registered = False
#
#     if request.method == "POST":
#         form = UserForm(data=request.POST)
#         if form.is_valid():
#
#             user = form.save() #will return a user type
#             user.set_password(user.password) #taking from the form
#             user.save()
#             print(user.password)
#             print(user)
#             return HttpResponse('/base')
#
#     token = {}
#     token.update(csrf(request))
#     token['form'] = form
#
#     #return render_to_response('userSignup.html', RequestContext(request, token))
#     return render(request, 'userSignup.html', token)

def confirmUser(request):
    return render(request, 'confirmUser.html')

def uploadReport(request):
    # user_name = request.user
    # UserProfile = user.userprofile

    if request.method == 'POST':

        #handle request later
        # sender = request.POST.get('from_name', '')
        # recipient = request.POST.get('to_name', '' )
        # messagebody = request.POST.get('message_content','')
        #
        # messageObj=Message(sender=sender, recipient=recipient, messagebody=messagebody)
        #
        # messageObj.save()

        files = request.FILES.getlist('report_file')
        report_form = ReportForm(request.POST, request.FILES)
        reports = Report.objects.all()

        if form.is_valid():
            report = report_form.save()

            for f in files:
                newFile = multipleFiles(f)
                newFile.save()
                report.report_file.add(newFile)

            report.save()
            return HttpResponse('VALID!')
        #     {
        #     'report_file_name': form.cleaned_data['report_file_name'],
        #     'company_name': form.cleaned_data['company_name'],
        #     'current_projects': form.cleaned_data['current_projects']
        # }

    else:
        report_form = ReportForm()
    return render(request, 'uploadReport.html', {'report_form': report_form});

#def viewReport(request)link from upload to report id. ex. http:127.800.000/showReport/viewReport/reportid/1

def groupSignup(request):
    if request.method == "POST":
        form = createGroupForm(data=request.POST)
        if form.is_valid():
            group = form.save()
            group.save()
            return HttpResponseRedirect('/confirmGroup/')

        else:
            print(form.errors)
    else:
        form = createGroupForm()
        # return HttpResponse("Invalid input")
        #user.groups.add in views.py
    return render(request, 'groupSignup.html', {'form': form})

def base(request):
    if request.method == "GET":
        return render(request, 'base.html', {'badLogin': 0})
    else:
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'base.html', {'badLogin': 0})
        else:
            return render(request, 'base.html', {'badLogin': 1})


def loggingOut(request):
    logout(request)
    return render(request, 'base.html', {'badLogin': 0})

def confirmGroup(request):
    return render(request, 'confirmGroup.html')

def showReport(request):
    return render(request, 'showReport.html')

def groupHome(request):
    return render(request, 'groupHome.html')

def groupLogin(request):
    return render(request, 'groupLogin.html')

def register(request):
    #context = RequestContext(request)
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()
            user.set_password(user.password)
            user.save()


            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            registered = True
            return HttpResponseRedirect('/confirmUser/')

        else:
            print(user_form.errors, profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    # Render the template depending on the context.
    return render(request,
            'userSignup.html', {'user_form': user_form, 'profile_form': profile_form, 'registered': registered})

def user_login(request):
    # Like before, obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':
        # Gather the username and password provided by the user.
        # This information is obtained from the login form.
        username = request.POST['username']
        password = request.POST['password']

        # Use Django's machinery to attempt to see if the username/password
        # combination is valid - a User object is returned if it is.
        user = authenticate(username=username, password=password)

        # If we have a User object, the details are correct.
        # If None (Python's way of representing the absence of a value), no user
        # with matching credentials was found.
        if user:
            # Is the account active? It could have been disabled.
            if user.is_active:
                # If the account is valid and active, we can log the user in.
                # We'll send the user back to the homepage.
                login(request, user)
                return HttpResponseRedirect('base.html')
            else:
                # An inactive account was used - no logging in!
                return HttpResponse("Your Rango account is disabled.")
        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {0}, {1}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    # The request is not a HTTP POST, so display the login form.
    # This scenario would most likely be a HTTP GET.
    else:
        # No context variables to pass to the template system, hence the
        # blank dictionary object...
        return render_to_response('login.html', {}, context)
