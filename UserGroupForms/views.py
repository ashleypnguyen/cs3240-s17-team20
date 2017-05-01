from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
#from django.core.context_processors import csrf
from django.template import loader
from .forms import ReportForm
from .models import User, Group, UserProfile
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
from django.db.models import Q
from django.contrib.postgres.search import SearchVector
import requests

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

    #if request.user.username != "":
    user_name = request.user
    users = UserProfile.objects.all().filter(user=user_name).first()
    # print(users)

    messages = Message.objects.all()
    count = 0
    for message in messages:
        if message.recipient == request.user.username:
            count += 1

    if request.method == 'POST':

        if report_form.is_valid():
            theReport = Report()
            theReport.created_by = users
            theReport.company_name = report_form.cleaned_data.get('company_name')
            theReport.ceo_name = report_form.cleaned_data.get('ceo_name')
            theReport.company_phone = report_form.cleaned_data.get('company_phone')
            theReport.company_email = report_form.cleaned_data.get('company_email')
            theReport.company_location = report_form.cleaned_data.get('company_location')
            theReport.company_country = report_form.cleaned_data.get('company_country')
            theReport.sector = report_form.cleaned_data.get('sector')
            theReport.business_type = report_form.cleaned_data.get('business_type')
            theReport.current_projects = report_form.cleaned_data.get('current_projects')
            theReport.private = report_form.cleaned_data.get('private')
            theReport.save()

        for f in request.FILES.getlist('htmlFile'):
            reportFile = File.objects.create(files = f)
            theReport.poodle.add(reportFile)
        theReport.save()
        return HttpResponseRedirect("base.html")
    return render(request, 'uploadReport.html', {'report_form': report_form, 'num_Messages': count})

def showReport(request):
    #allReports = Report.objects.all()
    user_name_2 = request.user
    user_for_report = UserProfile.objects.all().filter(user=user_name_2).first()
    allReports = Report.objects.all().filter(created_by=user_for_report)
    messages = Message.objects.all()
    count = 0
    for message in messages:
        if message.recipient == request.user.username:
            count += 1

    if request.method == 'POST':

        # return HttpResponse("POST WORKS")
        search_by_company_name = request.POST['search_by_company_name']
        search_by_ceo_name = request.POST['search_by_ceo_name']
        search_by_company_phone = request.POST['search_by_company_phone']
        search_by_company_email = request.POST['search_by_company_email']
        search_by_company_location = request.POST['search_by_company_location']
        search_by_company_country = request.POST['search_by_company_country']
        search_by_sector = request.POST['search_by_sector']
        search_by_business_type = request.POST['search_by_business_type']
        search_by_current_projects = request.POST['search_by_current_projects']
        select_and_or = request.POST['select_and_or']

        # return HttpResponse("IT WORKS")
        if(select_and_or=='and'):
            if(search_by_company_name and not search_by_company_name==''):
                allReports=allReports.filter(company_name = search_by_company_name)

            if (search_by_ceo_name and not search_by_ceo_name == ''):
                allReports = allReports.filter(ceo_name=search_by_ceo_name)

            if (search_by_company_phone and not search_by_company_phone == ''):
                allReports = allReports.filter(company_phone=search_by_company_phone)

            if (search_by_company_email and not search_by_company_email == ''):
                allReports = allReports.filter(company_phone=search_by_company_email)

            if(search_by_company_location and not search_by_company_location==''):
                allReports=allReports.filter(company_location = search_by_company_location)

            if(search_by_company_country and not search_by_company_country==''):
                allReports=allReports.filter(company_country = search_by_company_country)

            if (search_by_sector and not search_by_sector == ''):
                allReports = allReports.filter(business_type=search_by_sector)

            if(search_by_business_type and not search_by_business_type==''):
                allReports=allReports.filter(business_type = search_by_business_type)

            if(search_by_current_projects and not search_by_current_projects==''):
                allReports=allReports.filter(current_projects = search_by_current_projects)

        elif(select_and_or=='or'):
            query=Q()
            if(search_by_company_name):
                query |= Q(company_name=search_by_company_name)
            if (search_by_ceo_name):
                query |= Q(company_name=search_by_ceo_name)
            if (search_by_company_phone):
                query |= Q(company_phone=search_by_company_phone)
            if (search_by_company_email):
                query |= Q(company_phone=search_by_company_email)
            if(search_by_company_location):
                query |= Q(company_location=search_by_company_location)
            if(search_by_company_country):
                query |= Q(company_country=search_by_company_country)
            if (search_by_sector):
                query |= Q(company_phone=search_by_sector)
            if(search_by_business_type):
                query |= Q(business_type=search_by_business_type)
            if(search_by_current_projects):
                query |= Q(current_projects=search_by_current_projects)

            allReports=allReports.filter(query)

    # for r in allReports:
    #     listOfReports.append(r)
    #     for rf in r.reportFiles.all():
    #         fileList.append(rf)

    return render(request, 'showReport.html', {'allReports': allReports, 'num_Messages': count})
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
    messages = Message.objects.all()
    count = 0
    for message in messages:
        if message.recipient == request.user.username:
            count += 1
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
    return render(request, 'groupSignup.html', {'form': form, 'num_Messages': count})

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
            if user.is_active:
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
    messages = Message.objects.all()
    count = 0
    for message in messages:
        if message.recipient == request.user.username:
            count += 1
    return render(request, 'groupHome.html', {'num_Messages': count})

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
            user.is_active = True
            user.save()
            #
            # diffUser = User.objects.create_user(username, password=password)

            newProfile=UserProfile()

            newProfile.user=user
            print(user)
            #newProfile.user_type = False
            newProfile.save()


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


def my_user(request):
    user = None
    if request.user.is_authenticated():
        user = request.user

    return CustomUser.objects.get(username=user)

def user_search(request):
    tag = ""
    if request.method == 'POST':
        tag = request.POST['tag']
    query = Q()
    query |= Q(username__icontains=tag)
    query |= Q(first_name__icontains=tag)
    query |= Q(last_name__icontains=tag)
    query |= Q(email__icontains=tag)
    searched = User.objects.filter(query)
    return render(request, 'search.html', {'searched' : searched})

def sm(request):
    if request.method == "POST":
        if request.POST['sm_user'] != None:
            user = User.objects.get(username=request.POST['sm_user'])
            user.has_perm = True
            user.save()
        if request.POST['new_group'] != None:
            group = Group.objects.create(name=request.POST['new_group'])
            group.save()
        if request.POST['user_to_group'] != None and request.POST['group_for_user'] != None:
            user = User.objects.get(username=request.POST['user_to_group'])
            group = Group.objects.get(name=request.POST['group_for_user'])
            user.groups.add(group)
            user.save()
        if request.POST['user_from_group'] != None and request.POST['group_remove_user'] != None:
            user = User.objects.get(username=request.POST['user_from_group'])
            group = Group.objects.get(name=request.POST['group_remove_user'])
            user.groups.remove(group)
            user.save()
        if request.POST['suspended_user'] != None:
            user = User.objects.get(username=request.POST['suspended_user'])
            user.is_active = False
            user.save()
        if request.POST['restored_user'] != None:
            user = User.objects.get(username=(request.POST['restored_user'] + 'SUSPENDED'))
            user.is_active = True
            user.save()
        if request.POST['access_reports'] != None:
            user = User.objects.get(username=(request.POST['access_reports']))
            reports = Report.objects.filter(created_by=user)
        else:
            reports = Report.objects.all()
        if request.POST['delete_report'] != None:
            report = Report.objects.get(company_name=request.POST['delete_report'])
            report.delete()
        if request.POST['old_company_name'] != None:
            report = Report.objects.get(company_name=request.POST['old_company'])
            if request.POST['new_company_name'] != None:
                report.company_name = request.POST['new_company_name']
            if request.POST['new_ceo_name'] != None:
                report.ceo_name = request.POST['new_ceo_name']
            if request.POST['new_company_phone'] != None:
                report.company_phone = request.POST['new_company_phone']
            if request.POST['new_company_email'] != None:
                report.company_email = request.POST['new_company_email']
            if request.POST['new_company_location'] != None:
                report.company_location = request.POST['new_company_location']
            if request.POST['new_company_country'] != None:
                report.company_country = request.POST['new_company_country']
            if request.POST['new_sector'] != None:
                report.sector = request.POST['new_sector']
            if request.POST['new_business_type'] != None:
                report.business_type = request.POST['new_business_type']
            if request.POST['new_current_projects'] != None:
                report.current_projects = request.POST['new_current_projects']
            if request.POST['change_privacy_status']:
                report.private = not report.private
            report.save()
    else:
        reports = Report.objects.all()


    return render(request, 'sitemanager.html', {'reports' : reports})
