from django import forms
from .models import *

class PatientDetailsForm(forms.ModelForm):
    class Meta:
        model = PatientDetails
        fields = '__all__'

class ScreeningQuestionForm(forms.ModelForm):
    class Meta:
        model = ScreeningQuestionaire
        fields = '__all__'


class DemographicInfoForm(forms.ModelForm):
    class Meta:
        model = DemographicInfo
        fields = '__all__'


class CurrentIllnessInfoForm(forms.ModelForm):
    class Meta:
        model = CurrentIllnessInfo
        fields = '__all__'

class ChildrenInfoForm(forms.ModelForm):
    class Meta:
        model = ChildrenInfo
        fields = '__all__'

class RiskFactorsForm(forms.ModelForm):
    class Meta:
        model = RiskFactors
        fields = '__all__'

class PhysicalExaminationForm(forms.ModelForm):
    class Meta:
        model = PhysicalExamination
        fields = '__all__'


class DiseaseSeverityForm(forms.ModelForm):
    class Meta:
        model = DiseaseSverity
        fields = '__all__'


class VaccinationForm(forms.ModelForm):
    class Meta:
        model = Vaccination
        fields = '__all__'


class SpecimenCollectionForm(forms.ModelForm):
    class Meta:
        model = SpecimenCollection
        fields = '__all__'


class FinalOutcomeForm(forms.ModelForm):
    class Meta:
        model = FinalOutcome
        fields = '__all__'