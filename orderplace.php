<?php
   $place = $_REQUEST['place'];
   $name = $_REQUEST['pname'];
   $qua = $_REQUEST['pquantity'];
   $price = $_REQUEST['pprice'];
   $command_exec = escapeshellcmd('python orderplace.py'.' "'.$place.'" "'.$name.'" '.$qua.' '.$price);
   $str_output = shell_exec($command_exec);
   echo $str_output;
?>
