CREATE DATABASE KEMRI

use KEMRI
go;

CREATE TABLE LOGIN_USERS(
userid int primary key identity(1,1),
username varchar(60),
gender varchar(60),
contact int,
email varchar(560),
pass varchar(560),
created_at DATETIME DEFAULT GETDATE()
);


CREATE TABLE Screening (
	ID INT  UNIQUE  IDENTITY(1,1),
	patient_id VARCHAR(50) primary key,
	history_of_fever INT,
	body_temperature DECIMAL,
	coughing INT ,
	onset_of_symptoms INT,
	hospitalized VARCHAR,
	onset_date DATE,
	interview_type INT,
	createdby varchar(20),
	datecreated datetime DEFAULT GETDATE(),
);


CREATE TABLE Demographic (
	demographic_id INT PRIMARY KEY IDENTITY(1,1),
	patient_id VARCHAR(50),
	hospital_id varchar(100),
	interview_date DATE	,
	hospital_name varchar(100),
	age INT,
	years INT,
	sex INT,
	county varchar(100),
	village varchar(100),
	onset_of_current_illnes DATE,
	admission_date date,
	out_patient_date DATE,
	foreign key (patient_id) references Screening (patient_id),
	createdby varchar(100),
	datecreated datetime default getdate()
);


CREATE TABLE SignsSymptoms (
	symptoms_id INT PRIMARY KEY IDENTITY(1,1),
	patient_id VARCHAR(50),
	wheezing INT,
	sore_throat INT,
	breathing_difficulty INT,
	rhinorrhea INT,
	chest_pain INT,
	diarrhea INT,
	vomiting INT,
	muscle_aches INT,
	chills INT,
	appetite INT,
	convulsions INT,
	feeding INT,
	vomits INT,
	stridor INT,
	grunting INT,
	nasal_flaring INT,
	chest_in_drawing INT,
	lethargic INT,
	unconcious INT,
	foreign key (patient_id) references Screening (patient_id),
	createdby char(20),
	datecreated datetime default getdate()
);


CREATE TABLE RiskFactors (
	riskfactors_id INT PRIMARY KEY IDENTITY(1,1), 
	patient_id VARCHAR(50),
	chronicRespiratory INT,
	chronicNeurological INT,
	newlyDiagnosed INT,
	prior_tb INT,
	hivAids INT,
	chronicCardiac INT,
	malnutrition INT,
	chronicLiver INT,
	chronicRenal INT,
	diabetes INT,
	asthma INT,
	cancer INT,
	sickleCell INT,
	rickets INT,
	foreign key (patient_id) references Screening (patient_id),
	createdby varchar(100),
	datecreated datetime default getdate()
);

CREATE TABLE PhysicalExamination (
	examination_id INT PRIMARY KEY IDENTITY(1,1),
	patient_id VARCHAR(50),
	temperature float,
	type_of_measurement int,
	
	rate INT,
	oxygen INT,
	type_of_oxygen int,
	
	icu_hdu INT,
	mechanical_ventilation INT,
	foreign key (patient_id) references Screening (patient_id),
	createdby varchar(100),
	datecreated datetime default getdate()
);

CREATE TABLE Vaccination (
	vaccination_id INT PRIMARY KEY IDENTITY(1,1),
	patient_id VARCHAR(50),
	influenza INT,
	influenza_verification INT,
	covid_vaccine INT,
	covidVaccine_doses INT,
	covid19Verified INT,
	covid19Tested INT,
	covid19TestResult INT,
	patient_specimen INT,
	swab_type INT,
	collection_date DATE,
	foreign key (patient_id) references Screening (patient_id),
	createdby varchar(100),
	datecreated datetime default getdate()
);


CREATE TABLE FinalOutcome (
	outcome_id INT PRIMARY KEY IDENTITY(1,1),
	patient_id VARCHAR(50),
	final_outcome INT,
	other_facility varchar(200),
	final_outcomedate date,
	foreign key (patient_id) references Screening (patient_id),
	createdby varchar(100),
	datecreated datetime default getdate()
);


SELECT * FROM LOGIN_USERS

SELECT * FROM Screening
SELECT * FROM Demographic
SELECT * FROM SignsSymptoms 
SELECT * FROM RiskFactors
SELECT * FROM PhysicalExamination
SELECT * FROM Vaccination
SELECT * FROM FinalOutcome
