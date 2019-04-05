from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm
from .models import Contact, Donor, Needblood


# Create your views here.

def AboutView(request):
    return render(request,'blooddonationsystem/About.html',{})
def FeedbackView(request):
    return render(request,'blooddonationsystem/Feedback.html',{})
def ContactView(request):
    context={'contactdetails':Contact.objects.all()}
    return render(request,'blooddonationsystem/Contact.html',{})

def AddView(request):
    context={'donordetails':Donor.objects.all()}
    return render(request,'blooddonationsystem/adddonor.html',{})
def donor_details_form(request):
    res = "--->>>you are not eligible....!"
    print("hiiiiii")
    donor = Donor()
    try:
        donor.firstname = request.POST["firstname"]
        donor.lastname = request.POST["lastname"]
        donor.gender = request.POST["gender"]
        donor.email = request.POST["email"]
        donor.contactno = request.POST["contactno"]
        donor.DOB = request.POST["dateofbirth"]
        donor.major = request.POST["ismajor"]
        donor.Age = request.POST["isweight"]
        donor.nationality = request.POST["nation"]
        donor.bloodgroup = request.POST["Bloodgroup"]
        donor.Address = request.POST["address"]
        if donor.major=='no':
            return render(request, 'blooddonationsystem/adddonor.html', {'major': res})
        else:
            donor.save()

        return render(request, 'blooddonationsystem/adddonor.html', {})

    except ValueError:
     return render(request, 'blooddonationsystem/adddonor.html', {})

def Contact_details(request):
    contact = Contact()
    contact.name=request.POST["name"]
    contact.email=request.POST["email"]
    contact.contactnumber=request.POST["contactnumber"]
    contact.message=request.POST["message"]
    contact.save()
    return render(request, 'blooddonationsystem/Contact.html', {})

def need_blood_details(request):
     print("helloooooo")
     try:
         need = Needblood()
         need.firstname = request.POST["firstname"]
         need.lastname = request.POST["lastname"]
         need.gender = request.POST["gender"]
         need.email = request.POST["email"]
         need.contactno = request.POST["contactnumber"]
         need.DOB = request.POST["dateofbirth"]
         need.major = request.POST["major"]
         need.bloodgroup = request.POST["bloodgroup"]
         need.save()
         return render(request, 'blooddonationsystem/NeedBlood.html', {})
     except ValueError:
         return render(request, 'blooddonationsystem/NeedBlood.html', {})



def LoginView(request):
    form=UserCreationForm
    return render(request,'blooddonationsystem/LoginPage.html',{'form':form})
def NeedView(request):
    context={'needblooddetails':Needblood.objects.all()}
    return render(request,'blooddonationsystem/NeedBlood.html',{})
