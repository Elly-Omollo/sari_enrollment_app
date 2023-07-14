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
			   font-family: sans-serif;
				
			   display: grid;
    height: 100%;
    width: 100%;
    place-items: center;
    background-color: #186375;
	background: -webkit-linear-gradient(left, #073950, #36445e);

   
			  
				  background-color: #f2f2f2;
				  width: 100%;
				  height: 100vh;
				  font-family: Arial, sans-serif;
			  ;
 
			  }
			  .LogIn{
				  width:300px;
				  height:auto;
				  margin:auto;
				  background:white;
				  border-radius:33px
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
				   height: 30px;
				   border: 1px solid grey;
				   border-radius: 10px;
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
		
					
					//header('location:http://localhost/web_app/signin.php');
					
				}
			} else {
				echo "User not found. Please register an account.";
				
				header('location:http://localhost/web_app/register.html');
			}
		}
		
		sqlsrv_close($conn);
		?>
		

		<div class="LogIn">
			<h1>Log In</h1>
			
			<form action="signin.php" method="POST">
                <label></label>
				<input type="email" name = "email" placeholder="Email" required>
                <label></label>
				<input type="password" name = "pass" placeholder="Password"required>
				<input type="submit" name="submit" value="SUBMIT">

			</form>
			<p> Not have an account?<a href="register.html">Sign Up here</a></p>
			<div class='resetpassword'>
						<p><a href='forgotpass.php' >Forgot password:</a><p>
			</div>
		</div>

	</body>
</html>
