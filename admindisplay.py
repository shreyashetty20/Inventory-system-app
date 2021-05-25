#!/usr/bin/env python

import mysql.connector

connection = mysql.connector.connect(host="sql6.freesqldatabase.com",user="sql6414152",password="hnnpBcxV2a",database="sql6414152",port=3306)
cur = connection.cursor()


sql_select_Query = "select * from orplace"
cur.execute(sql_select_Query)
records = cur.fetchall()

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

print('''

<!DOCTYPE html>
<html>
<head>
<title>Dashboard</title>
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
margin-left: 26cm;
 color: black;
 padding: 1cm;

}
h1{
  text-align: center;
  font-size: 1cm;

}
body {font-family: Arial, Helvetica, sans-serif;
             background-repeat: no-repeat;
              font-family: "Times New Roman";
            

           
  background-size: cover;}
* {box-sizing: border-box;


}
html{ background-image: url(kk.jpg);}

 
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
table, th {
 

  border: 1px solid white;
  padding: .2cm;
 width: 10cm;
 background:black;
 margin-right: 3cm;
 color: white;
font-weight: bold;}

</style>
<body>
  <center>

 <form method="POST" action="" enctype="multipart/form-data">

<table>
  <thead>
<th>TOTAL ORDERS PLACED <br><br>'''+ str(cur.rowcount) + '''

</th>

<br>
<br>
<br>
<br>

<table>
  <thead>
    <th> TOTAL INCOME GENERATED <br><br>Rs. &nbsp''')

sql_select_Query = "SELECT quantity,price FROM orplace"
cur.execute(sql_select_Query)
records = cur.fetchall()

quan = 0
sumq = 0
price = 0
tot = 0.0
cur.execute("select * from securitykey3")
for row in records:
   record1 = cur.fetchone()
   p = int(record1[0])
   key = int(record1[1])
   q = int(record1[2])
   x = []
   x = list(map(int, row[0].split()))  
   dr_msg = decrypt(x, p, key, q)
   dmsg = ''.join(dr_msg)
   quan = int(dmsg)
   sumq = sumq + quan
   
   x = []
   x = list(map(int, row[1].split()))  
   dr_msg = decrypt(x, p, key, q)
   dmsg = ''.join(dr_msg)
   price = int(dmsg)
   
   tot = tot + (quan*price)

print(str(tot))

print('''
</th>
<br>
<br>
<br>

<br>    

<table>
  <thead>
    <th> PRODUCTS REMAINING<br><br>''')

cur.execute("SELECT * FROM product")
records = cur.fetchall()

cur.execute("select * from securitykey2")
sum1 = 0
for row in records:
   record1 = cur.fetchone()
   p = int(record1[0])
   key = int(record1[1])
   q = int(record1[2])
   x = []
   x = list(map(int, row[2].split()))  
   dr_msg = decrypt(x, p, key, q)
   dmsg = ''.join(dr_msg)
   sum1 += int(dmsg)

if(records == []) :
    pro = sum1
else :
    pro = sum1 - sumq
print(str(pro))

print( '''
</th>
<br>
<br>
<br>
<br>
</thead>
</table>
</table>
</form>
</center>
  </body>
</html>

''')

cur.close()
connection.close()
