<?php
   $name = $_REQUEST['name'];
   $email = $_REQUEST['email'];
   $phone = $_REQUEST['phone'];
   $command = escapeshellcmd('python register.py'.' '.$name.' '.$email.' '.$phone);
   $str_output = shell_exec($command);
   echo $str_output;
?>
