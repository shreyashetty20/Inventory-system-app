<?php
   $command_exec = escapeshellcmd('python new2.py');
   $str_output = shell_exec($command_exec);
   echo $str_output;
?>