from django.contrib import admin
from django.contrib.admin import AdminSite
from .models import *

# Register your models here.



class PatientDetailsAdmin(admin.ModelAdmin):
    search_fields = ['patient']
    list_display = ( 'patientId', 'hospitalID', 'interview_date')
    

admin.site.register(PatientDetails, PatientDetailsAdmin)



class ScreeningQuestionnaireAdmin(admin.ModelAdmin):
    search_fields = ['interview_type']
    list_display = ('patient', 'history_of_fever_report',"body_temperature", 'cough', 'onset_of_symptoms', 'hospitalized', 'onset_date', 'interview_type')
    

admin.site.register(ScreeningQuestionaire, ScreeningQuestionnaireAdmin)


class DemographicInfoAdmin(admin.ModelAdmin):
    search_fields = ['hospital_name']
    list_display = ('patient', 'hospital_name',"patients_age_in_months", 'patients_age_in_years', 'gender', 'county', 'village')
    

admin.site.register(DemographicInfo, DemographicInfoAdmin)


class CurrentIllnessInfoAdmin(admin.ModelAdmin):
    search_fields = ['']
    list_display = (
        'patient',
        'onset_date',
        'date_for_hospital_admision',
        'date_of_outpatient',
        'wheezing',
        'sore_throat',
        'difficulty_in_breathing',
        'rhinorrhea',
        'chest_pain',
        'diarrhea',
        'vomiting',
        'muscles_aches',
        'chills',
        'lack_of_appetite',
        'convulsions',
    )


admin.site.register(CurrentIllnessInfo, CurrentIllnessInfoAdmin)


class ChildrenInfoAdmin(admin.ModelAdmin):
    search_fields = ['']
    list_display = (
        'patient',
        'unable_to_drink',
        'vomits',
        'stridor',
        'grunting',
        'nasal_flaring',
        'chest_in_drawing',
        'lethargic',
        'unconcious',
        
    )


admin.site.register(ChildrenInfo, ChildrenInfoAdmin)


class RiskFactorsAdmin(admin.ModelAdmin):
    search_fields = ['']
    list_display = (
        'patient',
        'chronic_respiratory_disease',
        'neurological_disease',
        'newly_diagonised_TB',
        'prior_TB',
        'HIV_AIDS',
        'chardiac_heart_disease',
        'liver_disease',
        'diabetess',
        'asthma',
        'cancer',
        'sickle_cell',
        'rickets',
        
        
    )


admin.site.register(RiskFactors, RiskFactorsAdmin)


class PhysicalExaminationAdmin(admin.ModelAdmin):
    search_fields = ['']
    list_display = (
        'patient',
        'temperature',
        'mode_of_measurement',
        'respiratory_rate',
        'oxygent_saturation',
        'type_of_oxygen',
       
    )


admin.site.register(PhysicalExamination, PhysicalExaminationAdmin)


class DiseaseSverityAdmin(admin.ModelAdmin):
    search_fields = ['']
    list_display = (
        'patient',
        'admitted_to_ICU',
        'recieved_mechanicla_ventilation',
        
    )


admin.site.register(DiseaseSverity, DiseaseSverityAdmin)


class VaccinationAdmin(admin.ModelAdmin):
    search_fields = ['*']
    list_display = (
        'patient',
        'infuenza_vaccine',
        'influenza_verification',
        'covid_19',
        'number_of_covid_doses',
        'covid_19_test_verified_card',
        'covid_19_result',
        
    )


admin.site.register(Vaccination, VaccinationAdmin)


class SpecimenCollectionAdmin(admin.ModelAdmin):
    search_fields = ['*']
    list_display = (
        'patient',
        'specimen_collected',
        'type_of_spacimen_collected',
        'date_of_specimen_collection',
      
        
    )


admin.site.register(SpecimenCollection, SpecimenCollectionAdmin)



class FinalOutcomeAdmin(admin.ModelAdmin):
    search_fields = ['*']
    list_display = (
        'patient',
        'final_outcome',
        'refered_facility_name',
        'date_of_final_outcome',
      
        
    )


admin.site.register(FinalOutcome, FinalOutcomeAdmin)

