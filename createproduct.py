#!/usr/bin/env python

print('''
<!DOCTYPE html>
<html>
<head>
<title>ADD PRODUCT</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<nav class="topnav">
 <h2 class="logo">NIDHI's &nbsp INVENTORY &nbsp MANAGEMENT</h2>
  <a href="index.html">logout</a>
 <a href="clientorder.php" class="order">Order</a>
  <a href="createproduct.php" class="pro">Product</a>
  <a href="admindisplay.php" class="dash">Dashboard</a>

</nav>

<style>
body {font-family: Arial, Helvetica, sans-serif;
background:grey;
            background-repeat: no-repeat;
            -webkit-background-size: cover;
 font-family: "Times New Roman";
           
  background-size: cover;}
* {box-sizing: border-box;}
body {
  margin: 0;
  font-family: Arial, Helvetica, sans-serif;
}

.topnav {
  overflow: hidden;
  background-color: black;
   font-family: "Times New Roman";

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
  color: #f2f2f2;
  text-align: center;
  padding: 0.8cm 0.8cm;
  padding-left: 0.6cm;
  padding-right: 0.6cm;
  padding-bottom: 0.4cm;
  text-decoration: none;
  font-size: 17px;
   font-family: "Times New Roman";

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
.container {
  padding: 16px;
  background-color: white;
}

/* Full-width input fields */
input[type=text], input[type=file],input[type=number]{
  width: 100%;
  padding: 15px;
  margin: 5px 0 22px 0;
  display: inline-block;
  border: none;
  background: #f1f1f1;
}

input[type=text]:focus, input[type=file]:focus input[type=number]:focus{
  background-color: #ddd;
  outline: none;
}

/* Overwrite default styles of hr */
hr {
  border: 1px solid #f1f1f1;
  margin-bottom: 25px;
}

/* Set a style for the submit button */
.registerbtn {
  background-color: #4CAF50;
  color: white;
  padding: 16px 20px;
  margin: 8px 0;
  border: none;
  cursor: pointer;
  width: 100%;
  opacity: 0.9;
}

.registerbtn:hover {
  opacity: 1;
}
table

{

border-style:solid;

border-width:2px;
margin-left: 1.5cm;


border-color:pink;

}
table

{

border-style:solid;

border-width:2px;
margin-left: 1.5cm;


border-color:pink;

}
/* Add a blue text color to links */
a {
  color: dodgerblue;
}
h1{
  text-align: center;
}
/* Set a grey background color and center the text of the "sign in" section */
.signin {
  background-color: #f1f1f1;
  text-align: center;
}
.container .btn {
  background-color: #4CAF50;
  color: white;
  padding: 16px 20px;
  border: none;
  cursor: pointer;
  width: 25%;
  margin-bottom:10px;
  opacity: 0.8;
  margin-top: 2.3cm;
  margin-left: 7.5cm;
}
.container .cancel {
  background-color: red;
  color: white;
  padding: 16px 20px;
  border: none;
  cursor: pointer;
  width: 25%;
  margin-bottom:10px;
  opacity: 0.8;
  margin-top: 0cm;
}
.btn1 {
  background-color: #FFA500;
  color: white;
  padding: 16px 20px;
  text-align: center;
  border: none;
  cursor: pointer;
  width: 7.5cm;
  margin-bottom:3px;
  opacity: 0.8;
  
 
}
.container select{
 padding: 15px;
  margin: 5px 0cm 22px 0cm;
  display: inline-block;
  border: none;
  background: #f1f1f1;
  width: 370px;
}
.botton{
padding-left: 1cm;
padding-right:  1cm;
padding-top:  0.3cm;
padding-bottom: 0.3cm;
background-color: #ADD8E6;
border: none;
}

</style>
</head>
<body>
  
     <h1 id="messagedisplay">+ADD PRODUCT</h1>
   
<form method="POST" action="new2.php">
       <button type="submit"  class="btn1">DISPLAY AVAILABLE PRODUCTS</button>
       
     </form>
<form method="POST" action="createproduct.php" class="form-container" enctype="multipart/form-data">
  <div class="container">
   
    <hr>
    <label for="image"><b>Product Id</b></label><br><br>
    <input type="number" placeholder="Enter product id" name="image" required>
    
    <label for="Pro_name"><b>Product name</b></label>
    <input type="text" placeholder="Enter name" name="product_name" id="product_name" required>
    
    <label for="quantity"><b>Quantity</b></label>
    <input type="number" placeholder="Enter quantity" name="quantity" id="quantity" required>

    <label for="price"><b>Price</b></label>
    <input type="number" placeholder="Enter price" name="price" id="price" required>
    <div class="input-group">
      <button type="submit" class="btn" name="reg_user">Submit</button> 
	</form>
	<br>
	<br>
	<form method="POST" action="">
	  <button type="submit" class="btn cancel" name="cancel">Cancel</button>
	 </form>
    
</br>
 </div>
    

 
</body>
</html>  
''')  
   
    

import sys

product_name=sys.argv[2]
id1=str(sys.argv[1])
quantity=str(sys.argv[3])
price=str(sys.argv[4])

#storing in database

import mysql.connector

#connection = pymysql.connect(host="localhost",user="root",password="",database="inventory" )
connection = mysql.connector.connect(host="sql6.freesqldatabase.com",user="sql6414152",password="hnnpBcxV2a",database="sql6414152",port=3306)
cur = connection.cursor()


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
  
# Modular exponentiation
def power(a, b, c):
    x = 1
    y = a
  
    while b > 0:
        if b % 2 == 0:
            x = (x * y) % c;
        y = (y * y) % c
        b = int(b / 2)
  
    return x % c
  
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
  
def decrypt(en_msg, p, key, q):
  
    dr_msg = []
    h = power(p, key, q)
    for i in range(0, len(en_msg)):
        dr_msg.append(chr(int(en_msg[i]/h)))
          
    return dr_msg
  
# Driver code
def encryption():
    
    msg1 = product_name
    msg2 = id1
    msg3 = quantity
    msg4= price
    
    q = random.randint(pow(10, 20), pow(10, 50))
    g = random.randint(2, q)
    k = gen_key(q)# Private key for sender
    
    key = gen_key(q)# Private key for receiver
    h = power(g, key, q)
    
    
    en_msg1, p = encrypt(msg1, q, h, g, k)
    
    
    en_msg2, p = encrypt(msg2, q, h, g, k)
    
    
    en_msg3, p = encrypt(msg3, q, h, g, k)

    
    en_msg4, p = encrypt(msg4, q, h, g, k)
    
    
    string_ints1 = [str(int) for int in en_msg1]
    en1 = " ".join(string_ints1)
    
   
    string_ints2 = [str(int) for int in en_msg2]
    en2 = " ".join(string_ints2)
   
    string_ints3 = [str(int) for int in en_msg3]
    en3 = " ".join(string_ints3)

    string_ints4 = [str(int) for int in en_msg4]
    en4 = " ".join(string_ints4)

    
    cur.execute("insert into product values(%s,%s,%s,%s)",(en1,en2,en3,en4))
    cur.execute("insert into securitykey2 values(%s,%s,%s)",(str(p),str(key),str(q)))
    
    connection.commit()
    
    
  
encryption()

cur.close()
connection.close()
