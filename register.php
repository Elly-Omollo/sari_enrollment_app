<?php

session_start();

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
    echo 'connected';

    // Retrieve form data
    
    $username = $_POST["username"];
    $gender = $_POST["gender"];
    $contact = $_POST["contact"];
    $pass = password_hash($_POST["pass"], PASSWORD_DEFAULT);
    $email = $_POST["email"];

    // Check if the username already exists
    $sql = "SELECT * FROM LOGIN_USERS WHERE username = ?";
    $params = array($username);
    $stmt = sqlsrv_query($conn, $sql, $params);
    if ($stmt === false) {
        die(print_r(sqlsrv_errors(), true));
    }
    if (sqlsrv_has_rows($stmt)) {
        echo "Username already exists. Please choose a different username.";
        sqlsrv_free_stmt($stmt);
        sqlsrv_close($conn);
        exit();
    }
    sqlsrv_free_stmt($stmt);

    // Insert the new user into the database
    $sql = "INSERT INTO LOGIN_USERS (username, gender, contact, email, pass) VALUES (?, ?, ?,?, ?)";
    $params = array($username, $gender, $contact, $email, $pass );
    $stmt = sqlsrv_query($conn, $sql, $params);
    
    if ($stmt === false) {
        die(print_r(sqlsrv_errors(), true));
    }

    // Close the database connection
    sqlsrv_free_stmt($stmt);
    sqlsrv_close($conn);

    
header('location:http://localhost/web_app/signin.php');

echo "Registration successful!";
sqlsrv_close($conn);

}
?>
