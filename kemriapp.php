<?php
error_reporting(0);




if ($_SERVER['REQUEST_METHOD'] === 'POST') {

// Database connection
$serverName = "DESKTOP-FGIDCT8\SQLEXPRESS05";
$connectionOptions = array(
    "Database" => "KEMRI",
    "Uid" => "",
    "PWD" => ""
);

$conn = sqlsrv_connect($serverName, $connectionOptions);

if ($conn === false) {
    die(print_r(sqlsrv_errors(), true));
}


// Retrieve value from the previous table
$sql= "SELECT username FROM LOGIN_USERS ORDER BY userid DESC";

$stmt = sqlsrv_query($conn, $sql);

if ($stmt === false) {
    die(print_r(sqlsrv_errors(), true));
}

$createdby = '';



// Fetch the value from the previous table
if ($row = sqlsrv_fetch_array($stmt, SQLSRV_FETCH_ASSOC)) {
    $createdby = $row['username'];
}

// Retrieve form data
$history_of_fever = $_POST['history_of_fever'];
$body_temperature = $_POST['body_temperature'];
$coughing = $_POST['coughing'];
$onset_of_symptoms = $_POST['onset_of_symptoms'];
$hospitalized = $_POST['hospitalized'];
$onset_date = $_POST['onset_date'];
$interview_type = $_POST['interview_type'];
$patient_id = $_POST['patient_id'];
$hospital_id = $_POST['hospital_id'];
$interview_date = $_POST['interview_date'];
$hospital_name = $_POST['hospital_name'];
$age = $_POST['age'];
$years = $_POST['years'];
$sex = $_POST['sex'];
$county = $_POST['county'];
$village = $_POST['village'];
$onset_of_current_illnes = $_POST['onset_of_current_illnes'];
$admission_date = $_POST['admission_date'];
$out_patient_date = $_POST['out_patient_date'];
$wheezing = $_POST['wheezing'];
$sore_throat = $_POST['sore_throat'];
$breathing_difficulty = $_POST['breathing_difficulty'];
$rhinorrhea = $_POST['rhinorrhea'];
$chest_pain = $_POST['chest_pain'];
$diarrhea = $_POST['diarrhea'];
$vomiting = $_POST['vomiting'];
$muscle_aches = $_POST['muscle_aches'];
$chills = $_POST['chills'];
$appetite = $_POST['appetite'];
$convulsions = $_POST['convulsions'];
$feeding = $_POST['feeding'];
$vomits = $_POST['vomits'];
$stridor = $_POST['stridor'];
$grunting = $_POST['grunting'];
$nasal_flaring = $_POST['nasal_flaring'];
$chest_in_drawing = $_POST['chest_in_drawing'];
$lethargic = $_POST['lethargic'];
$unconcious = $_POST['unconcious'];
$chronicRespiratory =$_POST['chronicRespiratory'];
        $chronicNeurological =$_POST['chronicNeurological'];
        $newlyDiagnosed =$_POST['newlyDiagnosed'];
        $prior_tb =$_POST['prior_tb'];
        $hivAids =$_POST['hivAids'];
        $chronicCardiac =$_POST['chronicCardiac'];
        $malnutrition =$_POST['malnutrition'];
        $chronicLiver =$_POST['chronicLiver'];
        $chronicRenal =$_POST['chronicRenal'];
        $diabetes =$_POST['diabetes'];
        $asthma =$_POST['asthma'];
        $cancer =$_POST['cancer'];
        $sickleCell =$_POST['sickleCell'];
        $rickets =$_POST['rickets'];

        $temperature =$_POST['temperature'];
        $type_of_measurement =$_POST['type_of_measurement'];
        
        $rate =$_POST['rate'];
        $oxygen =$_POST['oxygen'];
        $type_of_oxygen =$_POST['type_of_oxygen'];
        
        $icu_hdu =$_POST['icu_hdu'];
        $mechanical_ventilation =$_POST['mechanical_ventilation'];

        $influenza =$_POST['influenza'];
        $influenza_verification =$_POST['influenza_verification'];
        $covid_vaccine =$_POST['covid_vaccine'];
        $covidVaccine_doses =$_POST['covidVaccine_doses'];
        $covid19Verified =$_POST['covid19Verified'];
        $covid19Tested =$_POST['covid19Tested'];
        $covid19TestResult =$_POST['covid19TestResult'];
        $patient_specimen =$_POST['patient_specimen'];
        $swab_type =$_POST['swab_type'];
        $collection_date=$_POST['collection_date'];

        $final_outcome = $_POST['final_outcome '];
        $other_facility = $_POST['other_facility'];
        $final_outcomedate = $_POST['final_outcomedate'];

// ... add more form field values as needed

// Insert values into the new table
$insertSql =  "INSERT INTO Screening (
	history_of_fever ,
	body_temperature ,
	coughing ,
	onset_of_symptoms ,
	hospitalized	 ,
	onset_date ,
	interview_type   ,
	patient_id ,
    createdby) VALUES (?, ?, ? ,?, ?, ?, ? ,?,?)";
    $params = array($history_of_fever ,
        $body_temperature ,
        $coughing ,
        $onset_of_symptoms ,
        $hospitalized ,
        $onset_date ,
        $interview_type ,
        $patient_id, 
        $createdby);
$insertStmt = sqlsrv_query($conn, $insertSql, $params);

if ($insertStmt === false) {
    die(print_r(sqlsrv_errors(), true));
}

// DEMOGRAPHIC TABLE
$demosql ='INSERT INTO Demographic
(
hospital_id
,patient_id
,interview_date
,hospital_name
,age
,years
,sex
,county
,village
,onset_of_current_illnes
,admission_date
,out_patient_date
,createdby)
VALUES
(?,?,?,?,?,?,?,?,?,?,?,?,?)';
$params =array($hospital_id
,$patient_id
,$interview_date
,$hospital_name
,$age
,$years
,$sex
,$county
,$village
,$onset_of_current_illnes
,$admission_date
,$out_patient_date
,$createdby);

$insertStmt = sqlsrv_query($conn, $demosql, $params);

if ($insertStmt === false) {
    die(print_r(sqlsrv_errors(), true));
}

$signssql= 'INSERT INTO  SignsSymptoms (
	patient_id ,
	wheezing ,
	sore_throat ,
	breathing_difficulty ,
	rhinorrhea ,
	chest_pain ,
	diarrhea ,
	vomiting ,
	muscle_aches ,
	chills ,
	appetite ,
	convulsions ,
	feeding ,
	vomits ,
	stridor ,
	grunting ,
	nasal_flaring ,
	chest_in_drawing ,
	lethargic ,
	unconcious ,
	createdby) 
    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)';
    $params = array(
        $patient_id ,
	    $wheezing ,
	    $sore_throat ,
	    $breathing_difficulty ,
	    $rhinorrhea ,
	    $chest_pain ,
	    $diarrhea ,
	    $vomiting ,
	    $muscle_aches ,
	    $chills ,
	    $appetite ,
	    $convulsions ,
	    $feeding ,
	    $vomits ,
	    $stridor ,
	    $grunting ,
	    $nasal_flaring ,
	    $chest_in_drawing ,
	    $lethargic ,
	    $unconcious ,
	    $createdby
    );

$insertStmt = sqlsrv_query($conn, $signssql, $params);

if ($insertStmt === false) {
    die(print_r(sqlsrv_errors(), true));
}


//RiskFactors table


$Risk= 'INSERT INTO  RiskFactors (
	patient_id ,
	chronicRespiratory ,
	chronicNeurological ,
	newlyDiagnosed ,
	prior_tb ,
	hivAids ,
	chronicCardiac ,
	malnutrition ,
	chronicLiver ,
	chronicRenal ,
	diabetes ,
	asthma ,
	cancer ,
	sickleCell ,
	rickets ,
	createdby) 
    VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)';
    $params = array(
        $patient_id ,
	    $chronicRespiratory ,
        $chronicNeurological ,
        $newlyDiagnosed ,
        $prior_tb ,
        $hivAids ,
        $chronicCardiac ,
        $malnutrition ,
        $chronicLiver ,
        $chronicRenal ,
        $diabetes ,
        $asthma ,
        $cancer ,
        $sickleCell ,
        $rickets ,
        $createdby
    );

$insertStmt = sqlsrv_query($conn, $Risk, $params);

if ($insertStmt === false) {
    die(print_r(sqlsrv_errors(), true));
}


//PhysicalExamination table
$Physical ='INSERT INTO PhysicalExamination (
	patient_id ,
	temperature ,
	type_of_measurement ,
	rate ,
	oxygen ,
	type_of_oxygen ,
	icu_hdu ,
	mechanical_ventilation ,
	createdby 
	)VALUES(?,?,?,?,?,?,?,?,?)';
     $params = array(
        $patient_id ,
        $temperature ,
        $type_of_measurement ,
        $rate ,
        $oxygen ,
        $type_of_oxygen ,
        $icu_hdu ,
        $mechanical_ventilation ,
        $createdby 
    );

$insertStmt = sqlsrv_query($conn, $Physical, $params);

if ($insertStmt === false) {
    die(print_r(sqlsrv_errors(), true));
}



//Vaccination table
$Vaccinetbl ='INSERT INTO Vaccination (
	patient_id ,
	influenza ,
	influenza_verification ,
	covid_vaccine ,
	covidVaccine_doses ,
	covid19Verified ,
	covid19Tested ,
	covid19TestResult ,
	patient_specimen ,
	swab_type ,
	collection_date ,
	createdby
	)VALUES(?,?,?,?,?,?,?,?,?,?,?,?)';
     $params = array(
        $patient_id ,
        $influenza ,
        $influenza_verification ,
        $covid_vaccine ,
        $covidVaccine_doses ,
        $covid19Verified ,
        $covid19Tested ,
        $covid19TestResult ,
        $patient_specimen ,
        $swab_type ,
        $collection_date,
        $createdby 
    );

$insertStmt = sqlsrv_query($conn, $Vaccinetbl, $params);

if ($insertStmt === false) {
    die(print_r(sqlsrv_errors(), true));
}

//FinalOutcome table
$Finaltbl ='INSERT INTO FinalOutcome (
	patient_id ,
	final_outcome ,
	other_facility ,
	final_outcomedate ,
	createdby
	)VALUES(?,?,?,?,?)';
     $params = array(
        $patient_id ,
        $final_outcome ,
        $other_facility ,
        $final_outcomedate ,
        $createdby
    );

$insertStmt = sqlsrv_query($conn, $Finaltbl, $params);

if ($insertStmt === false) {
    die(print_r(sqlsrv_errors(), true));
}

// Clean up resources
    header('location:http://localhost/web_app/kemriapp.html');
sqlsrv_free_stmt($stmt);
sqlsrv_close($conn);


}

?>


