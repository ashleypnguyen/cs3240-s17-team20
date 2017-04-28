from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
#from django.core.context_processors import csrf
from django.template import loader
from .forms import ReportForm
from .models import User, Group
from .models import Report
from .models import File
#from .models import Group
from .forms import UserForm, UserProfileForm, createGroupForm
from django.forms.models import model_to_dict
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from mailingsystem.models import Message

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


def confirmUser(request):
    return render(request, 'confirmUser.html')

def uploadReport(request):
    report_form = ReportForm(request.POST, request.FILES)

    if request.method == 'POST':

        if report_form.is_valid():
            theReport = Report()
            theReport.company_name = report_form.cleaned_data.get('company_name')
            theReport.company_phone = report_form.cleaned_data.get('company_phone')
            theReport.company_location = report_form.cleaned_data.get('company_location')
            theReport.company_country = report_form.cleaned_data.get('company_country')
            theReport.business_type = report_form.cleaned_data.get('business_type')
            theReport.current_projects = report_form.cleaned_data.get('current_projects')
            theReport.save()

        for f in request.FILES.getlist('htmlFile'):
            reportFile = File.objects.create(files = f)
            theReport.poodle.add(reportFile)
        theReport.save()
        return HttpResponseRedirect("base.html")
    return render(request, 'uploadReport.html', {'report_form': report_form})

def showReport(request):
    allReports = Report.objects.all()

    # for r in allReports:
    #     listOfReports.append(r)
    #     for rf in r.reportFiles.all():
    #         fileList.append(rf)

    return render(request, 'showReport.html', {'allReports': allReports})
    # reports = Report.objects.all()
    # if request.user.username != "":
    #     messages = Message.objects.all()
    #     count = 0
    #     for message in messages:
    #         if message.recipient == request.user.username:
    #             count += 1
    # return render(request, 'showReport.html', {'reports': reports, 'num_Messages': count})

        #
        #     r = report_form.save()
        #
        #     for f in files:
        #         newFile = multipleFiles(f)
        #         newFile.save()
        #         r.report_file.add(newFile)
        #
        #     r.save()
        #     return HttpResponse('base.html')
        # #     {
        #     'report_file_name': form.cleaned_data['report_file_name'],
        #     'company_name': form.cleaned_data['company_name'],
        #     'current_projects': form.cleaned_data['current_projects']
        # }
    #
    # else:
    #     report_form = ReportForm()
    #     if request.user.username != "":
    #         messages = Message.objects.all()
    #         count = 0
    #         for message in messages:
    #             if message.recipient == request.user.username:
    #                 count+=1
    # return render(request, 'uploadReport.html', {'report_form': report_form, 'num_Messages': count});

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
        if request.user.username != "":
            messages = Message.objects.all()
            count = 0
            for message in messages:
                if message.recipient == request.user.username:
                    count+=1
            return render(request, 'base.html', {'badLogin': 0, 'num_Messages': count})
        else:
            return render(request, 'base.html', {'badLogin': 0})
    else:
        username = request.POST['username']
        password = request.POST['pass']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages = Message.objects.all()
            count = 0
            for message in messages:
                if message.recipient == request.user.username:
                    count += 1
            return render(request, 'base.html', {'badLogin': 0, 'num_Messages': count})
        else:
            return render(request, 'base.html', {'badLogin': 1})


def loggingOut(request):
    logout(request)
    return render(request, 'base.html', {'badLogin': 0})

def confirmGroup(request):
    return render(request, 'confirmGroup.html')

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
