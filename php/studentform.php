<?php

/*
session_start();

// Database connection
$serverName = "DESKTOP-FGIDCT8\SQLEXPRESS01";
$connectionOptions = array(
    "Database" => "KEMRI",
    "Uid" => "",
    "PWD" => ""
);

$conn = sqlsrv_connect($serverName, $connectionOptions);

if ($conn === false) {
    die(print_r(sqlsrv_errors(), true));
}

// Retrieve values from the HTML form
$student_name = $_POST["student_name"];
$gender = $_POST["gender"];
$contact = $_POST["contact"];
$class = $_POST["class"];
$email = $_POST["email"];

// Retrieve value from the previous table
$created_by = '';

// Check if the user is logged in
if (isset($_SESSION['userid'])) {
    // Retrieve the logged-in user's name from the Users table
    $userid = $_SESSION['userid'];
    $sql = "SELECT userid FROM USERS WHERE userid = ?";
    $params = array($userid);
    $stmt = sqlsrv_query($conn, $sql, $params);

    if ($stmt === false) {
        die(print_r(sqlsrv_errors(), true));
    }

    if ($row = sqlsrv_fetch_array($stmt, SQLSRV_FETCH_ASSOC)) {
        $created_by = $row['userid'];
    }

    sqlsrv_free_stmt($stmt);
}


// ... add more form field values as needed

// Insert values into the new table
$insertSql = "INSERT INTO stsudentstbl (student_name, gender, contact, email, class, created_by) VALUES (?, ?, ?, ?, ?, ?)";
$params = array($student_name, $gender, $contact, $email, $class, $created_by);
$insertStmt = sqlsrv_query($conn, $insertSql, $params);

if ($insertStmt === false) {
    die(print_r(sqlsrv_errors(), true));
}

// Clean up resources
header('location:http://localhost/login%20page%20/studentform.html');
sqlsrv_free_stmt($stmt);
sqlsrv_close($conn);

*/


// Database connection
$serverName = "DESKTOP-FGIDCT8\SQLEXPRESS01";
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
$sql= "SELECT username FROM USERS ORDER BY userid DESC";
//$sql = "SELECT username FROM USERS";
$stmt = sqlsrv_query($conn, $sql);

if ($stmt === false) {
    die(print_r(sqlsrv_errors(), true));
}

$created_by = '';

// Fetch the value from the previous table
if ($row = sqlsrv_fetch_array($stmt, SQLSRV_FETCH_ASSOC)) {
    $created_by = $row['username'];
}

// Retrieve values from the HTML form
    $student_name = $_POST["student_name"];
    $gender = $_POST["gender"];
    $contact = $_POST["contact"];
    $class = $_POST["class"];
    $email = $_POST["email"];
// ... add more form field values as needed

// Insert values into the new table
$insertSql = "INSERT INTO stsudentstbl (student_name ,
gender ,
contact ,
email ,
class,
created_by) VALUES (?,?, ?, ?,?, ?)";
$params = array($student_name, $gender, $contact, $email, $class ,$created_by);
$insertStmt = sqlsrv_query($conn, $insertSql, $params);

if ($insertStmt === false) {
    die(print_r(sqlsrv_errors(), true));
}

// Clean up resources
    
header('location:http://localhost/login%20page%20/studentform.html');
sqlsrv_free_stmt($stmt);
sqlsrv_close($conn);




?>


