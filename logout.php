<?php
session_start(); // Ensure the session is active

// Clear all session variables
$_SESSION = array();

// Destroy the session
session_destroy();

// Redirect the user to the login page or any other desired page

header('location:http://localhost/web_app/signin.php');
exit();
?>
