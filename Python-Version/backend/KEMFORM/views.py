from django.shortcuts import redirect, render
from userauth.models import User
from django.contrib import messages
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
    if request.method == 'POST':
        form= PatientDetailsForm(request.POST or None)
        if form.is_valid():
            patientId = form.cleaned_data.get('patientId')
            hospitalID = form.cleaned_data.get('hospitalID')
            form.save()
            print(f'Sucesss, {patientId} and {hospitalID} ')
            return redirect('patient-screening')
        else:
            print('A user with these details already exist')
            return redirect('patient-details')
    else:
        form = PatientDetailsForm()
    return render(request, 'app/patientDetails.html', {'form':form})


# Csreening
def patientScreening(request):
    if request.method == 'POST':
        form = ScreeningQuestionForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully submited')
            print('================ Success ===============')
            return redirect('demographic')

        else:
            print('================== Invaalid =================')
            return redirect('patient-screening')
    else:
        form = ScreeningQuestionForm()
    return render(request, 'app/patientScreening.html', {'form':form})



# demographic
def demographicInfo(request):
    if request.method == 'POST':
        form = DemographicInfoForm( request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully submited')
            print('================ Success ===============')
            return redirect('current-illness')

        else:
            print('================== Invaalid =================')
            return redirect('demographic')

        
    else:
        form = DemographicInfoForm()
    return render(request, 'app/demographicInfo.html', {'form':form})



def currentIllnessInfo(request):
    if request.method == 'POST':
        form = CurrentIllnessInfoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Submited")
            print('Submited')
            return redirect('children-info')

        else:
            messages.error(request,'Invalid data please try again')
            print('Invalid data please try again')
            return redirect('current-illness')   
        pass
    else:
        form = CurrentIllnessInfoForm()
    return render(request, 'app/currentIllnessInfo.html', {'form':form})


# children infos
def childrenInfo(request):
    if request.method == 'POST':
        form = ChildrenInfoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Submitted')
            return redirect('risk-factors')
        else:
            messages.error(request, 'Action arbotted')
            return redirect('children-info')
    else:
        form = ChildrenInfoForm()
    return render(request, 'app/childrenInfo.html', {'form':form})

# risks factors
def risksFactors(request):
    if request.method == 'POST':
        form = RiskFactorsForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Submitted')
            return redirect('physical-examinations')
        else:
            messages.error(request, 'Action aborted')
            return redirect('risk-factors')
    else:
        form = RiskFactorsForm()
    return render(request, 'app/risksFactors.html', {'form':form})


def physicalExamination(request):
    if request.method == 'POST':
        form = PhysicalExaminationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Submitte')
            return redirect('disease-soverity')
        else:
            messages.error(request, 'Abortted')
            return redirect('physical-examinations')
    else:
        form = PhysicalExaminationForm()
    return render(request, 'app/physicalExamination.html', {'form':form})

# disease Soverity
def diseaseSverity(request):
    if request.method == 'POST':
        form = DiseaseSeverityForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Submitted')
            return redirect('vaccination')
        else:
            messages.error(request, 'Abortted')
            return redirect('disease-soverity')
    else:
        form = DiseaseSeverityForm()
   
    
    return render(request, 'app/diseaseSverity.html', {'form':form})

def vaccination(request):
    if request.method == 'POST':
        form = VaccinationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Submitted')
            return redirect('spacimen-collection')
        else:
            messages.error(request, 'Abortted')
            return redirect('vaccination')
    else:
        form = form = VaccinationForm()

    return render(request, 'app/vaccination.html', {'form':form})

def specimenCollection(request):
    if request.method == 'POST':
        form = SpecimenCollectionForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Submitted')
            return redirect('finall-outcome')
        else:
            messages.error(request, 'Abortted')
            return redirect('spacimen-collection')
    else:
        form = SpecimenCollectionForm()

    
    return render(request, 'app/specimenCollection.html', {'form':form})

def finalOutcome(request):
    if request.method == 'POST':
        form = FinalOutcomeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Submitted')
            return redirect('home')
        else:
            messages.error(request, 'Abortted')
            return redirect('finall-outcome')
    else:
        form = FinalOutcomeForm()

    
    return render(request, 'app/finalOutcome.html', {'form':form})