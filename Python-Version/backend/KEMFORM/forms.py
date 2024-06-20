from django import forms
from .models import *

class PatientDetailsForm(forms.ModelForm):
    class Meta:
        model = PatientDetails
        fields = '__all__'
        widgets = {
            'patientId':forms.TextInput(attrs={'class':'form-control'}),
            'hospitalID':forms.TextInput(attrs={'class':'form-control'}),
           
            
        }

class ScreeningQuestionForm(forms.ModelForm):
    class Meta:
        model = ScreeningQuestionaire
        fields = '__all__'
        widgets = {
            'patient':forms.Select(attrs={'class':'form-control'}),
            'history_of_fever_report':forms.Select(attrs={'class':'form-control'}),
            'body_temperature':forms.Select(attrs={'class':'form-control'}),
            'cough':forms.Select(attrs={'class':'form-control'}),
            'onset_of_symptoms':forms.Select(attrs={'class':'form-control'}),
            'hospitalized':forms.Select(attrs={'class':'form-control'}),
            'onset_date':forms.DateInput( attrs={'class':'form-control ', 'type': 'date'}),
            'interview_type':forms.Select(attrs={'class':'form-control'}),
            # 'interview_date': forms.DateInput(attrs={'class': 'form-control datepicker', 'placeholder': 'Interview Date'})
        }



class DemographicInfoForm(forms.ModelForm):
    class Meta:
        model = DemographicInfo
        fields = '__all__'
        widgets = {
            'patient':forms.Select(attrs={'class':'form-control'}),
            'hospital_name':forms.TextInput(attrs={'class':'form-control'}),
            'patients_age_in_months':forms.TextInput(attrs={'class':'form-control'}),
            'patients_age_in_years':forms.TextInput(attrs={'class':'form-control'}),
            'gender':forms.Select(attrs={'class':'form-control'}),
            'county':forms.TextInput(attrs={'class':'form-control'}),
            'village':forms.TextInput(attrs={'class':'form-control '}),
            

        }


class CurrentIllnessInfoForm(forms.ModelForm):
    class Meta:
        model = CurrentIllnessInfo
        fields = '__all__'
        widgets = {
            'patient':forms.Select(attrs={'class':'form-control'}),
            'onset_date':forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'date_for_hospital_admision':forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            'date_of_outpatient':forms.DateInput(attrs={'class':'form-control' , 'type':'date'}),
            'wheezing':forms.Select(attrs={'class':'form-control'}),
            'sore_throat':forms.Select(attrs={'class':'form-control'}),
            'difficulty_in_breathing':forms.Select(attrs={'class':'form-control', 'placeholder': 'Interview Date'}),
            'rhinorrhea':forms.Select(attrs={'class':'form-control'}),
            'chest_pain':forms.Select(attrs={'class':'form-control'}),
            'diarrhea':forms.Select(attrs={'class':'form-control'}),
            'vomiting':forms.Select(attrs={'class':'form-control'}),
            'muscles_aches':forms.Select(attrs={'class':'form-control'}),
            'chills':forms.Select(attrs={'class':'form-control'}),
            'lack_of_appetite':forms.Select(attrs={'class':'form-control'}),
            'convulsions':forms.Select(attrs={'class':'form-control'}),
            # 'interview_date': forms.DateInput(attrs={'class': 'form-control datepicker', 'placeholder': 'Interview Date'})
        }





class ChildrenInfoForm(forms.ModelForm):
    class Meta:
        model = ChildrenInfo
        fields = '__all__'
        widgets = {
            'patient':forms.Select(attrs={'class':'form-control'}),
            'unable_to_drink':forms.Select(attrs={'class':'form-control'}),
            'vomits':forms.Select(attrs={'class':'form-control'}),
            'stridor':forms.Select(attrs={'class':'form-control'}),
            'wheezing':forms.Select(attrs={'class':'form-control'}),
            'grunting':forms.Select(attrs={'class':'form-control'}),
            'nasal_flaring':forms.Select(attrs={'class':'form-control datepicker', 'placeholder': 'Interview Date'}),
            'chest_in_drawing':forms.Select(attrs={'class':'form-control'}),
            'lethargic':forms.Select(attrs={'class':'form-control'}),
            'unconcious':forms.Select(attrs={'class':'form-control'}),
            
        }

        



class RiskFactorsForm(forms.ModelForm):
    class Meta:
        model = RiskFactors
        fields = '__all__'
        widgets = {
            'patient':forms.Select(attrs={'class':'form-control'}),
            'chronic_respiratory_disease':forms.Select(attrs={'class':'form-control'}),
            'neurological_disease':forms.Select(attrs={'class':'form-control'}),
            'newly_diagonised_TB':forms.Select(attrs={'class':'form-control'}),
            'prior_TB':forms.Select(attrs={'class':'form-control'}),
            'HIV_AIDS':forms.Select(attrs={'class':'form-control'}),
            'chardiac_heart_disease':forms.Select(attrs={'class':'form-control '}),
            'malnutrition':forms.Select(attrs={'class':'form-control datepicker'}),
            'liver_disease':forms.Select(attrs={'class':'form-control'}),
            'renal_disease':forms.Select(attrs={'class':'form-control'}),
            'diabetess':forms.Select(attrs={'class':'form-control'}),
            'asthma':forms.Select(attrs={'class':'form-control'}),
            'cancer':forms.Select(attrs={'class':'form-control'}),
            'sickle_cell':forms.Select(attrs={'class':'form-control'}),
            'rickets':forms.Select(attrs={'class':'form-control'}),
        }


class PhysicalExaminationForm(forms.ModelForm):
    class Meta:
        model = PhysicalExamination
        fields = '__all__'
        widgets ={
            'patient':forms.Select(attrs={'class':'form-control'}),
            'temperature':forms.TextInput(attrs={'class':'form-control'}),
            'mode_of_measurement':forms.Select(attrs={'class':'form-control'}),
            'respiratory_rate':forms.TextInput(attrs={'class':'form-control'}),
            'oxygent_saturation':forms.TextInput(attrs={'class':'form-control'}),
            'type_of_oxygen':forms.Select(attrs={'class':'form-control'}),
            
        }


class DiseaseSeverityForm(forms.ModelForm):
    class Meta:
        model = DiseaseSverity
        fields = '__all__'
        widgets = {
            'patient':forms.Select(attrs={'class':'form-control'}),
            'admitted_to_ICU':forms.Select(attrs={'class':'form-control'}),
            'recieved_mechanicla_ventilation':forms.Select(attrs={'class':'form-control'}),
           
        }


class VaccinationForm(forms.ModelForm):
    class Meta:
        model = Vaccination
        fields = '__all__'
        widgets = {
            'patient':forms.Select(attrs={'class':'form-control'}),
            'infuenza_vaccine':forms.Select(attrs={'class':'form-control'}),
            'influenza_verification':forms.Select(attrs={'class':'form-control'}),
            'covid_19':forms.Select(attrs={'class':'form-control'}),
            'number_of_covid_doses':forms.TextInput(attrs={'class':'form-control'}),
            'covid_19_test_verified_card':forms.Select(attrs={'class':'form-control'}),
            
            'covid_19_result':forms.Select(attrs={'class':'form-control'}),
            
        }


class SpecimenCollectionForm(forms.ModelForm):
    class Meta:
        model = SpecimenCollection
        fields = '__all__'
        widgets ={
            'patient':forms.Select(attrs={'class':'form-control'}),
            'specimen_collected':forms.Select(attrs={'class':'form-control'}),
            'type_of_spacimen_collected':forms.Select(attrs={'class':'form-control'}),
            'date_of_specimen_collection':forms.DateInput(attrs={'class':'form-control', 'type':'date'}),
            
        }


class FinalOutcomeForm(forms.ModelForm):
    class Meta:
        model = FinalOutcome
        fields = '__all__'
        widgets = {
            'patient':forms.Select(attrs={'class':'form-control'}),
            'final_outcome':forms.Select(attrs={'class':'form-control'}),
            'refered_facility_name':forms.TextInput(attrs={'class':'form-control'}),
            'date_of_final_outcome':forms.DateInput(attrs={'class':'form-control','type':'date'}),
            
        }