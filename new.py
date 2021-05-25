#!/usr/bin/env python

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


sql_select_Query = "select * from product"
register = cur.execute(sql_select_Query)
# get all records
records = cur.fetchall()
    

cur.execute("select * from securitykey2")


print('''
<!DOCTYPE html>
<html>
<head>
  <title>PRODUCT</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<nav class="topnav">
  <h2 class="logo">NIDHI's &nbsp INVENTORY &nbsp MANAGEMENT</h2>
  <a href="index.html">logout</a>
  <a href="order.php" class="order">Order</a>
  <a href="new.php" class="pro">Product</a>
  <a href="dashboard.html" class="dash">Dashboard</a>
 
 
 
</nav>
<style>
body {font-family: Arial, Helvetica, sans-serif;


            background-repeat: no-repeat;
            -webkit-background-size: cover;
           
  background-size: cover;}
* {box-sizing: border-box;
}

html{ background-image: url(kk.jpg);}
.topnav {
font-family: "Times New Roman";
  overflow: hidden;
  background-color: black;

}
.logo{
font-family: "Times New Roman";
  float: left;
  font-size: 0.6cm;
  padding-left: 0.5cm;
  padding-top: 0.4cm;
  padding-bottom: 0.4cm;
  color:  white;
  font-style: sans-serif;
}
.topnav a {
  float: right;
  color: white;
  text-align: center;
  padding: 0.8cm 0.8cm;
  padding-left: 0.6cm;
  padding-right: 0.6cm;
  text-decoration: none;
  font-size: 17px;

 }

.topnav a:hover {
  background-color: #ddd;
  color: black;
}

.topnav a.active {
  background-color: #4CAF50;
  color: white;
}
.tp{
  padding: 0.5cm;
  background-color: #9ee6d8;
  color: #455ca8;
  margin-top: 2cm;
}
.tp:hover {
  background-color: #5F9EA0;
  color: black;
}

.tp.active {
  background-color: #5F9EA0;
  color: white;
}
.to{
  padding: 0.5cm;
  background-color: #9ee6d8;
  color: #455ca8;
  margin-top: 2cm;
}
.to:hover {
  background-color: #5F9EA0;
  color: black;
}

.to.active {
  background-color: #5F9EA0;
  color: white;
}
.tr{
  padding: 0.5cm;
  background-color: #9ee6d8;
  color: #455ca8;
  margin-top: 2cm;
}
.tr:hover {
  background-color: #5F9EA0;
  color: black;
}

.tr.active {
  background-color: #5F9EA0;
  color: white;
}
table, th, td {
  border: 1px solid black;
  background:#f5f5f5;
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
body {
            background-image: url(kk.jpg);
            background-repeat: no-repeat;
            -webkit-background-size: cover;

            
  background-size: cover;
  
  
  
}
</style>
<body>


  <center>
<br><br><br><br><br>
<table>
  <thead>
    <tr>
<th>PRODUCT ID</th>
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
       x = list(map(int, row[1].split()))  

       dr_msg = decrypt(x, p, key, q)
       dmsg = ''.join(dr_msg)
       print('''<tr><td>''')
       print(dmsg)
       print('''</td>''')
       
       x = []
       x = list(map(int, row[0].split()))
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
       print(dmsg)
       print('''</td>''')
             
       x = []
       x = list(map(int, row[3].split()))
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
