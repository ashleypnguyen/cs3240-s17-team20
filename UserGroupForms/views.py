from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.template import loader
from .forms import ReportForm
from .forms import UserForm
from .forms import createGroupForm
from .models import User
from .models import Report
from .models import Group

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

def userSignup(request):
    if request.method == "POST":
        form = UserForm(data=request.POST)
        if(form.is_valid()):
            form.save()
            return HttpResponse("User has been registered.")
    else:
        form = UserForm()
        return render(request, 'userSignup.html', {'form': form})

def uploadReport(request):

    if request.method == 'POST':
        #handle request later

        form = ReportForm(request.POST, request.FILES)

        if form.is_valid():
            return render(request, 'showReport.html', {
            'report_file_name': form.cleaned_data['report_file_name'],
            'company_name': form.cleaned_data['company_name'],
            'current_projects': form.cleaned_data['current_projects']
        })

    else:
        form = ReportForm()
    return render(request, 'uploadReport.html', {'form': form});

#def viewReport(request)link from upload to report id. ex. http:127.800.000/showReport/viewReport/reportid/1

def groupSignup(request):
    if request.method == "POST":
        form = UserForm(data=request.POST)
        if (form.is_valid()):
            form.save()
            return HttpResponse("The group has been created!")
    else:
        form = UserForm()
        # return HttpResponse("Invalid input")
        return render(request, 'groupSignup.html', {'form': form})

def base(request):
    return render(request, 'base.html')