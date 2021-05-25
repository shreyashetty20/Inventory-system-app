#!/usr/bin/env python

#database
import mysql.connector

connection = mysql.connector.connect(host="sql6.freesqldatabase.com",user="sql6414152",password="hnnpBcxV2a",database="sql6414152",port=3306)
cur = connection.cursor()

def power(a, b, c):
    x = 1
    y = a
  
    while b > 0:
        if b % 2 == 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)
  
    return x % c

def decrypt(en_msg, p, key, q):
  
    dr_msg = []
    h = power(p, key, q)
    for i in range(0, len(en_msg)):
        dr_msg.append(chr(int(en_msg[i]/h)))
          
    return dr_msg

sql_select_Query = "select * from orplace"
register = cur.execute(sql_select_Query)
# get all records
records = cur.fetchall()
    

cur.execute("select * from securitykey3")



print('''<!DOCTYPE html>
<html>
<head>
  <title>PLACED ORDERS</title>
  <link rel="stylesheet" type="text/css" href="dash.css">
</head>
<nav class="topnav">
 <h2 class="logo">NIDHI's &nbsp INVENTORY &nbsp MANAGEMENT</h2>
 <a href="index.html">logout</a>
 <a href="clientorder.php" class="order">Order</a>
  <a href="createproduct.php" class="pro">Product</a>
  <a href="admindisplay.php" class="dash">Dashboard</a>

</nav>
<style>
 
  p{
font-size: 25px;
font-weight: bold;
font-style: oblique;
 color: black;
 padding: 1cm;

}
h1{
  text-align: center;
  font-size: 1cm;
}
body{
  background:url(l.jpg);
  background-repeat: no-repeat;
  background-size: cover;
}

  table, th, td {
  border: 1px solid #404040;
  background:white;
  color:black;
  font-weight: bold;

}
.btn1 {
  background-color: #FFA500;
  color: white;
  padding: 16px 20px;
  text-align: center;
  border: none;
  cursor: pointer;
  width: 7.5cm;
  margin-bottom:2px;
  opacity: 0.8;
 
  margin-top: 0.2cm;
}
</style>
<body>
  <center>

 <form method="POST" action="" enctype="multipart/form-data">
   
<h1>PLACED ORDERS</h1>


<table border='1'>
<table>
<thead>
<tr>
<th>CLIENT NAME</th>
<th>PHONE</th>
<th>PLACE</th>
<th>PRODUCT NAME</th>
<th>QUANTITY</th>
<th>PRICE</th>




</tr>
</thead>

''')
for row in records:
   record1 = cur.fetchone()
   if record1 != None  :
            
       p = int(record1[0])
       key = int(record1[1])
       q = int(record1[2])
            
       x = []
       x = list(map(int, row[0].split()))  

       dr_msg = decrypt(x, p, key, q)
       dmsg = ''.join(dr_msg)
       print('''<tr><td>''')
       print(dmsg.upper())
       print('''</td>''')
       
       x = []
       x = list(map(int, row[1].split()))
       print('''<td>''')
       dr_msg = decrypt(x, p, key, q)
       dmsg = ''.join(dr_msg)
       print(dmsg)
       print('''</td>''')
       
       
       x = []
       x = list(map(int, row[2].split()))
       print('''<td>''')
       dr_msg = decrypt(x, p, key, q)
       dmsg = ''.join(dr_msg)
       print(dmsg.upper())
       print('''</td>''')
             
       x = []
       x = list(map(int, row[3].split()))
       print('''<td>''')
       dr_msg = decrypt(x, p, key, q)
       dmsg = ''.join(dr_msg)
       print(dmsg.upper())
       print('''</td>''')

       x = []
       x = list(map(int, row[4].split()))
       print('''<td>''')
       dr_msg = decrypt(x, p, key, q)
       dmsg = ''.join(dr_msg)
       print(dmsg)
       print('''</td>''')
             
       x = []
       x = list(map(int, row[5].split()))
       print('''<td>''')
       dr_msg = decrypt(x, p, key, q)
       dmsg = ''.join(dr_msg)
       print(dmsg)
       print('''</td></tr>''')
       
print('''      
</table>
</form></center>
</body>
</html> ''')
