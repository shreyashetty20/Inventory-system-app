<?php
   $pid = $_REQUEST['image'];
   $pname = $_REQUEST['product_name'];
   $quan = $_REQUEST['quantity'];
   $price = $_REQUEST['price'];
   $command_exec = escapeshellcmd('python createproduct.py'.' '.$pid.' "'.$pname.'" '.$quan.' '.$price);
   $str_output = shell_exec($command_exec);
   echo $str_output;
?>
