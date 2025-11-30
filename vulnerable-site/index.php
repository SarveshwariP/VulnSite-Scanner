<?php
include "db.php";
if(isset($_POST['login'])){
$user=$_POST['username']; $pass=$_POST['password'];
$sql="SELECT * FROM users WHERE username='$user' AND password='$pass'";
$result=$conn->query($sql);
if($result->num_rows>0){ $r=$result->fetch_assoc(); header("Location: dashboard.php?user=".$r['id']); }
else{ echo "<p style='color:red'>Invalid Login</p>"; }}
?><h2>Login</h2><form method="POST"><input name="username"><br><input name="password"><br><button name="login">Login</button></form>