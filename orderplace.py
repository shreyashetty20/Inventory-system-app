#!/usr/bin/env python

#storing in database

import mysql.connector

#connection = pymysql.connect(host="localhost",user="root",password="",database="inventory" )
connection = mysql.connector.connect(host="sql6.freesqldatabase.com",user="sql6414152",password="hnnpBcxV2a",database="sql6414152",port=3306)
cur = connection.cursor()



import sys

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


sql_select_Query = "select * from register"
register = cur.execute(sql_select_Query)
records = cur.fetchall()[-1]
    

cur.execute("select * from securitykey")


record1 = cur.fetchall()[-1]
p = int(record1[0])
key = int(record1[1])
q = int(record1[2])
            
x = []
x = list(map(int, records[0].split()))
dr_msg = decrypt(x, p, key, q)
cname = ''.join(dr_msg)
    
x = []
x = list(map(int, records[2].split()))
dr_msg = decrypt(x, p, key, q)
cphone = ''.join(dr_msg)
 

name=cname
contact=cphone
place=sys.argv[1]
pname=sys.argv[2]
quantity=str(sys.argv[3])
price=str(sys.argv[4])


#Encrypting
import random 
from math import pow
  
a = random.randint(2, 10)
  
def gcd(a, b):
    if a < b:
        return gcd(b, a)
    elif a % b == 0:
        return b;
    else:
        return gcd(b, a % b)
  
# Generating large random numbers
def gen_key(q):
  
    key = random.randint(pow(10, 20), q)
    while gcd(q, key) != 1:
        key = random.randint(pow(10, 20), q)
  
    return key
  

# Asymmetric encryption
def encrypt(msg, q, h, g, k):
  
    en_msg = []
  
    s = power(h, k, q)
    p = power(g, k, q)
      
    for i in range(0, len(msg)):
        en_msg.append(msg[i])
  
    
    for i in range(0, len(en_msg)):
        en_msg[i] = s * ord(en_msg[i])
  
    return en_msg, p
  
# Driver code
def encryption():
    msg1=name
    msg2=contact
    msg3=place
    msg4=pname
    msg5=quantity
    msg6=price
    
    
    #msg1 = "shivani"
    #msg2 = "email"
    #msg3 = "8978978988"
    
    
    q = random.randint(pow(10, 20), pow(10, 50))
    g = random.randint(2, q)
    k = gen_key(q)# Private key for sender
    
    key = gen_key(q)# Private key for receiver
    h = power(g, key, q)
    
   
    en_msg1, p = encrypt(msg1, q, h, g, k)
    
    
    en_msg2, p = encrypt(msg2, q, h, g, k)
    
    
    en_msg3, p = encrypt(msg3, q, h, g, k)

    en_msg4, p = encrypt(msg4, q, h, g, k)
    
    en_msg5, p = encrypt(msg5, q, h, g, k)
    
    en_msg6, p = encrypt(msg6, q, h, g, k)
    
    
    
    string_ints1 = [str(int) for int in en_msg1]
    en1 = " ".join(string_ints1)
   
    string_ints2 = [str(int) for int in en_msg2]
    en2 = " ".join(string_ints2)
   
    string_ints3 = [str(int) for int in en_msg3]
    en3 = " ".join(string_ints3)

    string_ints4 = [str(int) for int in en_msg4]
    en4 = " ".join(string_ints4)
   
    string_ints5 = [str(int) for int in en_msg5]
    en5 = " ".join(string_ints5)
   
    string_ints6 = [str(int) for int in en_msg6]
    en6 = " ".join(string_ints6)

    
    cur.execute("insert into orplace values(%s,%s,%s,%s,%s,%s)",(en1,en2,en3,en4,en5,en6))
    cur.execute("insert into securitykey3 values(%s,%s,%s)",(str(p),str(key),str(q)))
    connection.commit()
    
encryption()

cur.close()
connection.close()


print(''' 
      
<!DOCTYPE html>
<html>
<head>
<title>Client</title>
<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
<nav class="topnav">
  <h2 class="logo">NIDHI's &nbsp INVENTORY &nbsp MANAGEMENT</h2>
  <a href="index.html">logout</a>
  <a href="order.php" class="order">Order</a>
  <a href="new.php" class="pro">Product</a>
  <a href="dashboard.html" class="dash">Dashboard</a>
 
 
 
 
</nav>
<style>
  .topnav {
  overflow: hidden;
  background-color: black;

}
.logo{
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
  color: #f2f2f2;
  text-align: center;
  padding: 0.8cm 0.8cm;
  padding-left: 0.6cm;
  padding-right: 0.6cm;
  text-decoration: none;
  font-size: 17px;

 }
 body {font-family: Arial, Helvetica, sans-serif;
             background-repeat: no-repeat;
              font-family: "Times New Roman";
            background-size: cover;
          }
* {box-sizing: border-box;

}
html{ background-image: url(kk.jpg);}

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
  </style>
<div class="header">
<h1>Order Placed Successfully</h1>
</div>


</body>
</html>

      ''')
