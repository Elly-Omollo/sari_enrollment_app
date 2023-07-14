<?php

//"select username from users where email ='ellyok@gmail.com'"

$serverName = "DESKTOP-FGIDCT8\SQLEXPRESS01";
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
/*
$sql = "select username from users where email ='ellyok@gmail.com'";
   // $params = array($email);
    $stmt = sqlsrv_query($conn, $sql);

    if ($stmt === false) {
        die(print_r(sqlsrv_errors(), true));
    }

    // Retrieve the value from the result
if ($row = sqlsrv_fetch_array($stmt, SQLSRV_FETCH_ASSOC)) {
    $value = $row['username'];
    echo "Retrieved value: " . $value;
} else {
    echo "No rows found";
}*/
?>


<?php
//session_start();

// Check if the email address is stored in the session variable
if (isset($_SESSION['email'])) {
    // Retrieve the email address from the session variable
    $email = $_SESSION['email'];

    // Display the email address on the registration form
    echo "Email Address: " . $email;

    

    // Perform other operations using the retrieved email address
    // For example, insert the email address into a table
    $sql = "INSERT INTO your_table (email) VALUES (?)";
    $params = array($email);
    $stmt = sqlsrv_query($conn, $sql, $params);

    if ($stmt === false) {
        die(print_r(sqlsrv_errors(), true));
    }

    // Clean up resources
    sqlsrv_free_stmt($stmt);
    sqlsrv_close($conn);

    // Unset the email session variable
    unset($_SESSION['email']);
} else {
    // Redirect to the login form if the email address is not available
    header("Location: login.php");
    exit();
}
?>

<!-- Registration Form HTML -->
<!-- Display other form elements -->
