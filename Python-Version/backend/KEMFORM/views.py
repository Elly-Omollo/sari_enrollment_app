from django.shortcuts import render
from userauth.models import User
from .forms import *
# Create your views here.

def home(request):

    user = User.objects.get(email = request.user.email)
    emial = user.email
    context = {
        'name': 'Elly Okinyi',
        'phone': 789456330,
        'email':'ellyok@gmail.com',
        'user':emial
        
    }
    return render(request, "app/index.html", context)



# form submission views
def patientDetails(request):
    form = PatientDetailsForm()
    return render(request, 'app/patientDetails.html', {'form':form})



def patientScreening(request):
    form = ScreeningQuestionForm()
    return render(request, 'app/patientScreening.html', {'form':form})


def demographicInfo(request):
    form = DemographicInfoForm()
    return render(request, 'app/demographicInfo.html', {'form':form})



def currentIllnessInfo(request):
    form = CurrentIllnessInfoForm()
    return render(request, 'app/currentIllnessInfo.html', {'form':form})



def childrenInfo(request):
    form = ChildrenInfoForm()
    return render(request, 'app/childrenInfo.html', {'form':form})


def risksFactors(request):
    form = RiskFactorsForm()
    return render(request, 'app/risksFactors.html', {'form':form})