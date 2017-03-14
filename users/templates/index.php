<!DOCTYPE html>
<html>
	<head>
		<meta charset="utf-8">
		<title>Strona Główna - Slight Learning</title>
		<link rel="stylesheet" href="style.css" />
	</head>
	<body>
		<div class="main-box">
			<div class="baner-box">
				<div id="logo"><a href="index.php"><img alt="" src="images/logo.png"></a></div>
				<div class="menu-top-box">
					<ol id="menu-top-ol">
						<li><a href="courses.php">KURSY</a></li>
						<li><a href="tests.php">TESTY</a></li>
						<li><a href="tasks.php">ZADANIA</a></li>
						<li><a href="faq.php">FAQ</a></li>
						<li><a href="about_us.php">O NAS</a></li>
						<li><a href="contact.php">KONTAKT</a></li>
					</ol>
				</div>
				<div class="login-box">
					<?php
						session_start();
						
						if (!isset($_SESSION['reg_id']))
						{
							session_regenerate_id();
							$_SESSION['reg_id'] = true;
						}
						
						if(isset($_SESSION['is_logged']))
						{
							if ($_SESSION['is_logged'] === hash('ripemd128', $_SERVER['REMOTE_ADDR'].$_SERVER['HTTP_USER_AGENT']))
							{
								echo '<div id="logged">Witaj, <a href="user.php">'.$_SESSION['forename'].'</a></div>';
								echo '<ol id="login-list">';
								echo '<li><a href="logout.php">Wyloguj</a></li></ol>';
							}
							else
							{
								session_unset();
								session_destroy();
								echo '<ol id="login-list">';
								echo '<li><a href="login.php">Zaloguj się</a></li>';
								echo '<li><a href="register.php">Rejestracja</a></li></ol>';
							}
						}
						
						else
						{
							echo '<ol id="login-list">';
							echo '<li><a href="login.php">Zaloguj się</a></li>';
							echo '<li><a href="register.php">Rejestracja</a></li></ol>';
						}
					?>
				</div>
				
			</div>
			<div class="content-box">
				<div id="m-content-box">
					<div id="content-box-top">
						Aktualności
					</div>
					<div id="content-box-bottom">
					
					</div>
				</div>
			</div>
			<div class="footer-box">
				<table>
					<tr><td id="foot-bar"></td></tr>
					<tr>
						<td id="first"><a href="faq.php">FAQ</a></td><td><a href="contact.php">Kontakt</a></td><td><a href="policies.php">Regulamin</a></td>
						<td id="cpright">Copyright © 2016 by Sebastian Dziula. All rights reserved</td>
					</tr>
				</table>
			</div>
		</div>
	</body>
</html>
