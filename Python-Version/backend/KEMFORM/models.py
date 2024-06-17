from django.db import models

# Create your models here.
RESPONSE_CHOICES = [
        ('yes', 'Yes'),
        ('no', 'No'),
        ('dont_know', "I don't know"),
    ]

INTERVIEW_CHOICES = [
    ('1','SARI surveillance'),
    ('2','Outbreak'),
    ('1','ILI surveillance'),
]

GENDER_CHOICES = [
    ('male','male'),
    ('female','female'),
]

COVID19_CHOICES = [
    ('positive','Positive'),
    ('negative','Negative'),
]

TEMPERATURE_CHOICES = [
    ('oral', 'Oral'),
    ('auxiliary', 'Auxiliary'),
]

OXYGEN_TYPE_CHOICES = [
    ('room_air', "Room Air"),
    ('on_supplemental_oxygen', "On Supplemental Oxygen"),
]


FINAL_CHOICES = [
    ('discharged_alive', 'Discharge from hospital alive'),
    ('death', 'Death'),
    ('refused_treatment', 'Refuse hospital tratment'),
    ('absconded', 'Absconded'), 
]


# patient details
class PatientDetails(models.Model):
    patientId = models.CharField(max_length=6,  unique=True)
    hospitalID = models.CharField(max_length=6, unique=True)
    interview_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.patientId}'

# screening questionss
class ScreeningQuestionaire(models.Model):
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    history_of_fever_report = models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name="Did the patient report a history of fever?")
    body_temperature = models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name="The patient has   measured fever greater than 38 ℃?")
    cough = models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name="Is the patient presenting with a cough?")
    onset_of_symptoms = models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name="Was the onset of symptoms within the last 10 days?")
    hospitalized = models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name="Has the patient been hospitalized?")
    onset_date = models.DateField(auto_now_add=False, verbose_name='Date of onset')


    interview_type = models.CharField(max_length=100, choices=INTERVIEW_CHOICES, verbose_name='What was the interview type?')
    
    def __str__(self):
        return f'{self.patient.patientId}'

class DemographicInfo(models.Model):
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    hospital_name = models.CharField(max_length=100)
    patients_age_in_months = models.IntegerField()
    patients_age_in_years = models.IntegerField()
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES)
    county = models.CharField(max_length=100)
    village = models.CharField(max_length=100)


    def __str__(self):
        return f'{self.hospital_name}'
    


class CurrentIllnessInfo(models.Model):
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    onset_date = models.DateField(auto_now_add=False)
    date_for_hospital_admision = models.DateField(auto_now_add=False)
    date_of_outpatient = models.DateField(auto_now_add=False)

    wheezing = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    sore_throat = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    difficulty_in_breathing = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    rhinorrhea = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    chest_pain = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    diarrhea = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    vomiting = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    muscles_aches = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    chills = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    lack_of_appetite = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    convulsions = models.CharField(max_length=10, choices=RESPONSE_CHOICES)



    def __str__(self):
        return f'{self.onset_date}'
    
class ChildrenInfo(models.Model):
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    unable_to_drink = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    vomits = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    stridor = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    grunting = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    nasal_flaring = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    chest_in_drawing = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    lethargic = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    unconcious = models.CharField(max_length=10, choices=RESPONSE_CHOICES)

    def __str__(self):
        return f'{self.unable_to_drink}'
    

class RiskFactors(models.Model):
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    chronic_respiratory_disease = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    neurological_disease = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    newly_diagonised_TB = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    prior_TB = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    HIV_AIDS = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    chardiac_heart_disease = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    liver_disease = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    renal_disease = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    diabetess = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    asthma = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    cancer = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    sickle_cell = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    rickets = models.CharField(max_length=10, choices=RESPONSE_CHOICES)

    def __str__(self):
        return f"{self.chardiac_heart_disease}"
    

class PhysicalExamination(models.Model):
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    temperature = models.FloatField()
    mode_of_measurement = models.CharField(max_length=100, choices=TEMPERATURE_CHOICES)
    respiratory_rate = models.CharField(max_length=100)
    oxygent_saturation = models.CharField(max_length=100)
    type_of_oxygen = models.CharField(max_length=100, choices=OXYGEN_TYPE_CHOICES)

    def __str__(self):
        return f'{self.temperature}'
    

# for SARI Cases only
class DiseaseSverity(models.Model):
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    admitted_to_ICU = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    recieved_mechanicla_ventilation = models.CharField(max_length=10, choices=RESPONSE_CHOICES)

    def __str__(self):
        return f'{self.admitted_to_ICU}'
    

class Vaccination(models.Model):
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    infuenza_vaccine = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    covid_19 =models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    number_of_covid_doses = models.IntegerField()
    covid_19_test_verified_card = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    covid_19_test = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    covid_19_result = models.CharField(max_length=10, choices=COVID19_CHOICES)

    def __str__(self):
        return f'{self.infuenza_vaccine}'
    

class SpecimenCollection(models.Model):
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    specimen_collected = models.CharField(max_length=10, choices=RESPONSE_CHOICES)
    type_of_spacimen_collected = models.CharField(max_length=100)
    date_of_specimen_collection = models.DateField()

    def __str__(self):
        return f'{self.date_of_specimen_collection}'


class FinalOutcome(models.Model):
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    final_outcome = models.CharField(max_length=100, choices=FINAL_CHOICES)
    refered_facility_name = models.CharField(max_length=100)
    date_of_final_outcome = models.DateField(auto_now_add=False)

    def __str__(self):
        return f'{self.date_of_final_outcome}'