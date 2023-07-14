<?php
session_start(); 
$serverName = "DESKTOP-FGIDCT8\SQLEXPRESS05";
$connectionOptions = array(
    "Database" => "KEMRI",
    "Uid" => "",
    "PWD" => ""
);


// Establish the connection
$conn = sqlsrv_connect($serverName, $connectionOptions);

if ($conn === false) {
    die(print_r(sqlsrv_errors(), true));
}

// Form submission handling
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $email = $_POST["email"];
    $pass = $_POST["pass"];

    // Check if the user exists
    $sql = "SELECT * FROM LOGIN_USERS WHERE email = ?";
    $params = array($email);
    $stmt = sqlsrv_query($conn, $sql, $params);

    if ($stmt === false) {
        die(print_r(sqlsrv_errors(), true));
    }

    if (sqlsrv_has_rows($stmt)) {
        $row = sqlsrv_fetch_array($stmt, SQLSRV_FETCH_ASSOC);
        $hashedPassword = $row["pass"];

        // Verify the password
        if (password_verify($pass, $hashedPassword)) {
            // Start the session
            session_start();

            // Store user information in session variables
            $_SESSION["username"] = $username;
            $_SESSION["email"] = $row["email"];

            // Redirect to the desired page after successful login
            header('location:http://localhost/web_app/kemriapp.html');

            exit();
        } else {
            echo "Invalid password.";

            
            header('location:http://localhost/web_app/signin.html');
            
        }
    } else {
        echo "User not found. Please register an account.";
        
        header('location:http://localhost/web_app/register.html');
    }
}

sqlsrv_close($conn);
?>
