<?php
   $command_exec = escapeshellcmd('python order.py');
   $str_output = shell_exec($command_exec);
   echo $str_output;
?>