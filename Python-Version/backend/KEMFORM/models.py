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
    ('forehead', 'Forehead thermometer gun'),
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

SPECIMEN_CHOICES = [
    ('nasal_swab', 'Nasal swab'),
    ('op', 'OP'),
    ('ip', 'IP'),
    ('ip/op', 'IP/OP'),
]


# patient details
class PatientDetails(models.Model):
    patientId = models.CharField(max_length=6,  unique=True, verbose_name='Patient unique ID number')
    hospitalID = models.CharField(max_length=6, unique=True, verbose_name='Hospital ID number')
    interview_date = models.DateField(auto_now_add=True, verbose_name='Interview date')

    def __str__(self):
        return f'{self.patientId}'

# screening questions
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
    # Demographic information
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    hospital_name = models.CharField(max_length=100, verbose_name='Hospital:')
    patients_age_in_months = models.IntegerField(verbose_name='Age in months(for children below 59 months)')
    patients_age_in_years = models.IntegerField(verbose_name='age in years ')
    gender = models.CharField(max_length=100, choices=GENDER_CHOICES, verbose_name="Sex")
    
    # where do you live?
    county = models.CharField(max_length=100)
    village = models.CharField(max_length=100)


    def __str__(self):
        return f'{self.hospital_name}'
    


class CurrentIllnessInfo(models.Model):
    # Date of current illness
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    onset_date = models.DateField(auto_now_add=False, verbose_name='Date of onset of current illness')
    date_for_hospital_admision = models.DateField(auto_now_add=False, null=True, verbose_name='Date of hospital admission(for SARI cases)') #for sari cases
    date_of_outpatient = models.DateField(auto_now_add=False, verbose_name='Date seen in out-patient(for ILI cases)')  #for ILI case

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
    # complete the following for children less than 5 yrs
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE )
    unable_to_drink = models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name='Unable to drink or breastfeed at all')
    vomits = models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name='Vomits everything')
    stridor = models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name='Stridor:')
    grunting = models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name='Grunting:')
    nasal_flaring = models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name='Nasal flaring:')
    chest_in_drawing = models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name='Chest in-dwrawing (reaction under ribcage on inspiration):')
    lethargic = models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name='Lethargic:')
    unconcious = models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name='Unconscious(comatos, not awake):')

    def __str__(self):
        return f'{self.unable_to_drink}'
    

class RiskFactors(models.Model):
    # Does the patient have any of the medical conditions listed below as diagnosed by a cllinician?
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    chronic_respiratory_disease = models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name='Chronic respiratory disease (not including asthma and TB)')
    neurological_disease = models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name='Chronic neurological or neuromuscular disease')
    newly_diagonised_TB = models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name='Newly diagnosed TB')
    prior_TB = models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name='Prior TB')
    HIV_AIDS = models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name='HIV/AIDS')
    chardiac_heart_disease = models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name='Chronic cardiac/heart disease')
    malnutrition = models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name='Malnutrition')
    liver_disease = models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name='Chronic liver disease')
    renal_disease = models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name='Chronic renal disease')
    diabetess = models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name='Diabetes')
    asthma = models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name='Asthma')
    cancer = models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name='Cancer (currently or in the past 12 months)')
    sickle_cell = models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name='Sickle cell disease')
    rickets = models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name='Rickets')

    def __str__(self):
        return f"{self.chardiac_heart_disease}"
    

class PhysicalExamination(models.Model):
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    temperature = models.FloatField(verbose_name='Temperature')
    mode_of_measurement = models.CharField(max_length=100, choices=TEMPERATURE_CHOICES, verbose_name='Mode of temperature measurement')
    # Oxygen saturation %:
    respiratory_rate = models.CharField(max_length=100,verbose_name='Respiratory rate: ( breaths per minute<strong><i>(count for full minute)')
    oxygent_saturation = models.CharField(max_length=100,verbose_name='Oxygen saturation %:')
    type_of_oxygen = models.CharField(max_length=100, choices=OXYGEN_TYPE_CHOICES, verbose_name='Type of oxygen')

    def __str__(self):
        return f'{self.temperature}'
    

# for SARI Cases only
class DiseaseSverity(models.Model):
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    # Has the patient:
    admitted_to_ICU = models.CharField(max_length=10, choices=RESPONSE_CHOICES,verbose_name='Been admitted to ICU/HDU?')
    recieved_mechanicla_ventilation = models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name='Received mechanical ventilation?')

    def __str__(self):
        return f'{self.admitted_to_ICU}'
    

class Vaccination(models.Model):
    # 15. Has the patient received any of the following vaccinations? (Ask to see vaccination card)
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    # 15 . a
    infuenza_vaccine = models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name='Influenza vaccine in the first twelve months?')
    influenza_verification =models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name='Was this verified using a vaccination card?')
    covid_19 =models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name='Covid 19 Vaccine?')
    number_of_covid_doses = models.IntegerField(verbose_name='If yes, how many doses of COVID-19 vaccine?')
    covid_19_test_verified_card = models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name='Was this verified using a vaccination card or hospital records?')
   
    covid_19_result = models.CharField(max_length=10, choices=COVID19_CHOICES, verbose_name='If yes, what was the COVID-19 test result?')

    def __str__(self):
        return f'{self.infuenza_vaccine}'
    

class SpecimenCollection(models.Model):
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    specimen_collected = models.CharField(max_length=10, choices=RESPONSE_CHOICES, verbose_name='Was any specimen collected from this patient for influenza testing?')
    type_of_spacimen_collected = models.CharField(max_length=100, choices=SPECIMEN_CHOICES, verbose_name='Type of swab specimen collected?')
    date_of_specimen_collection = models.DateField(verbose_name='Date of specimen collection')

    def __str__(self):
        return f'{self.date_of_specimen_collection}'


class FinalOutcome(models.Model):
    patient = models.ForeignKey(PatientDetails, on_delete=models.CASCADE)
    final_outcome = models.CharField(max_length=100, choices=FINAL_CHOICES, verbose_name='What was the final outcome?')
    refered_facility_name = models.CharField(max_length=100, verbose_name='Specify name of the facility' )
    date_of_final_outcome = models.DateField(auto_now_add=False, verbose_name='Date of final outcome?')

    def __str__(self):
        return f'{self.date_of_final_outcome}'