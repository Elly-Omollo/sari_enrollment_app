<!DOCTYPE html>
<html>
	<head>
		
		<meta charset="utf-8">
		<meta name="viewport" content="width=device-width,initial-scale=1">
		<link rel="stylesheet" href="../css/sign.css">
		<title>FORM LOGIN AND REGISTER</title>
		
		<style>
			
			body{
				background: grey;
				width:100%;
				height:100vh;
 
			  }
			  .LogIn{
				  width:300px;
				  height:300px;
				  margin:auto;
				  background:white;
				  border-radius:7px
				  }
			   h1{
				   text-align:center;
				   color:orange;
				   padding-top:12px;
				   }
		   
			   form{
				   width:300px;
				   color:pink;
				   height:auto;
				   margin-left:12px
				   
				   }
			   form label{
				   display:flex;
				   margin-top:20px;
				   font-size:18px;
				   }
			   form input{
				   width:90%;
				   padding:5px;
				   border:none;
				   border: 1px solid grey;
				   border-radius: 3px;
				   outline: none;
				   
				   }
			   input[type="submit"]{
				   width:250px;
				   height:40px;
				   margin-top:20px;
				   border:none;
				   background-color:violet;
				   color:white;
				   font-size:15px;
				   cursor:pointer;
				   
				   }
			   input[type="submit"]:hover{
				   font-size:20px;
				   background-color:green;
				   color:white;
				   width:280px;
				   
				   }
			   p{
				   text-align:center;
				   padding-top:20px;
				   font-size:15px;
				   }
				   .resetpassword.p{
					color:white;
				   }
	   
		</style>
	</head>
	<body>

    <?php
// Step 1: "Forgot Password" form
if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    // Retrieve the submitted email address
    $email = $_POST['email'];

    // Validate the email address (you can use additional validation techniques)
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        echo "Invalid email address.";
        exit();
    }
    

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


    try {
        // Prepare the select statement
        $tsql = "SELECT * FROM LOGIN_USERS WHERE email = ?";
        $params = array($email);
        $stmt = sqlsrv_query($conn, $tsql, $params);
//token generation
        function generateToken($length = 32) {
            $token = bin2hex(random_bytes($length));
            return $token;
        }
        // Check if the email exists
        if (sqlsrv_has_rows($stmt)) {
            // Generate a unique token
            $token = generateToken(); // You need to implement this function to generate a unique token
            $resetToken = password_hash($token, PASSWORD_DEFAULT);

            // Store the token in the database
            // Perform the necessary database query to store the token associated with the user's email

            $tsql = "UPDATE LOGIN_USERS SET pass = ? WHERE email = ?";
             $params = array(password_hash($token, PASSWORD_DEFAULT), $email);
             $stmt = sqlsrv_prepare($conn, $tsql, $params);

             if (sqlsrv_execute($stmt) === false) {
                 die( print_r(sqlsrv_errors(), true));
             }

             
     /*            // Send the password reset email to the user
    $resetLink = "http://example.com/reset_password.php?email=" . urlencode($email) . "&token=" . urlencode($token);

    $to = $email;
    $subject = "Password Reset";
    $message = "Click the link below to reset your password:\n\n" . $resetLink;
    $headers = "From: admin@example.com";

    if (mail($to, $subject, $message, $headers)) {
        // Email sent successfully, show a success message to the user
        echo "Password reset email has been sent to your email address.";
    } else {
        // Failed to send email, show an error message to the user
        echo "Failed to send password reset email.";
    }

    // Close the connection to the SQL Server
    sqlsrv_close($conn);
}*/

            // Send the password reset email to the user
            $resetLink = "https://example.com/reset_password.php?token=" . $token;
            $emailContent = "Click the following link to reset your password: $resetLink";
            mail($email, "Password Reset", $emailContent);

            echo "Password reset link has been sent to your email address.";

            // Redirect to the login page
header('location:http://localhost/web_app/signin.php');
            exit();
        } else {
            echo "Email address not found.";
        }
    } catch (Exception $e) {
        // Handle the exception
        echo "Error: " . $e->getMessage();
    }

    // Close the connection
    sqlsrv_close($conn);
}
?>

		

		<div class="LogIn">
			
        <h1>Reset Password</h1>
			
			<form action="#" method="POST">
                <label>Email</label>
				<input type="email" name = "email" required>
                <label>New Password</label>
				<input type="password" name = "pass" required>
				<input type="submit" name="submit" value="SUBMIT">

			</form>
            <p> Not have an account?<a href="register.html">Sign Up here</a></p>
			

	</body>
</html>
