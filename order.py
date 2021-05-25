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
    
    
print('''
<!DOCTYPE html>
<html>
<!--<link href="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/css/bootstrap.min.css" rel="stylesheet" id="bootstrap-css">-->
<script src="//maxcdn.bootstrapcdn.com/bootstrap/3.3.0/js/bootstrap.min.js"></script>
<script src="//code.jquery.com/jquery-1.11.1.min.js"></script>
<!------ Include the above in your HEAD tag ---------->
<html>
  <head>
   

<title>PLACING ORDER</title>

<nav class="topnav">
 <h2 class="logo">NIDHI's INVENTORY  MANAGEMENT</h2>
 <a href="index.html">logout</a>
 <a href="order.php" class="order">Order</a>
 <a href="new.php" class="pro">Product</a>
 <a href="dashboard.html" class="dash">Dashboard</a>

</nav>
</head>
<style>
.form-contro{
  padding: 1cm;
  border: solid black;
}
*
{
 
  box-sizing: content-box;
  color: inherit;
  font-family: inherit;
  font-size: inherit;
  font-style: inherit;
  font-weight: inherit;
  line-height: inherit;
  list-style: none;
  margin: 0;
  padding: 0.1cm;
  text-decoration: none;
  vertical-align: top;
}
.topnav {
  overflow: hidden;
  background-color: black;

}
h2{
  font-size: 0.7cm;
  margin-left:0.3cm;
}

.cancel {
  background-color: red;
  color: white;
  padding: 16px 20px;
  border: none;
  cursor: pointer;
  width: 15%;
  margin-bottom:10px;
  opacity: 0.8;
  margin-top: 4.3cm;
  margin-left: 23cm;
}
h1{
  text-align: center;
  padding: 0.4cm;
  background-color: grey;
}
.btn{
  background-color: #4CAF50;
  color: white;
  padding: 16px 20px;
  border: none;
  cursor: pointer;
  width: 15%;
  margin-bottom:10px;
  opacity: 0.8;
  margin-top: 2.3cm;
  margin-left: 3cm;
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
  padding-bottom: 0.4cm;
  text-decoration: none;
  font-size: 17px;

 }

.input label{
margin: 10px 10px 10px 0px;
}
.input label{
display: block;
text-align: left;
margin: 3px;
}
.input input{
height: 30px;
width: 10%;
padding: 5px 10px;
font-size: 16px;
border-radius: 5px;
border: 1px solid grey;

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
}.for
.input-group label{
margin: 10px 10px 10px 0px;
}
.input-group label{
display: block;
text-align: left;
margin: 3px;
}
.input-group input{
height: 30px;
width: 20%;
padding: 5px 10px;
font-size: 16px;
border-radius: 5px;
border: 1px solid black;
;
}
select {
display: block;
padding: 10px;
  width: 210px;
  background-color: #e0e0e0;
  border: none;
  box-shadow: 1px 1px 2px #bbbbbb;
  cursor: pointer;
 margin: 0;

 
}
form{
  text-align:"center";
}
.login label,
.login input {
   
    margin-left: 12px;
    padding: 10px;
   
width:30%;

}
.enter label,
.enter input {
   
    margin-left: 08px;
    padding: 10px;
   
width:30%;

}
.entr label,
.entr input {
   
    margin-left: 20px;
    padding: 10px;
   
width:30%;

}
.gt label,
.gt input {
   
    margin-left: 50px;
    padding: 20px;
   
width:30%;

}
h1{
  text-align: center;
  padding: 0.4cm;
  background-color: grey;
}
.input-group{
  margin-left: 0.5cm;
}
label{
  font-size: 0.5cm;
}

  </style>
<body>
<h1>Placing order</h1>
<br><br>
<h2>Adding client detail</h2>


</header>
<article>
<form action="orderplace.php" method="post">

<table class="meta">
 

<div class="input-group">
<label>Client name</label>
<input type="text" name="clientname" value="'''+cname+'''" disabled>

</div>
<div class="input-group">
<label>Client contact</label>
<input type="number" name="number" value="'''+cphone+'''" disabled>
</div>
<div class="input-group">
<label>Place</label>
<input type="text" name="place">
</div>
<div class="input-group">
  <label>Product name</label>
  <input type="text" name="pname">
  </div>

  <div class="input-group">
    <label>Product quantity</label>
    <input type="number" name="pquantity">
    </div>

    <div class="input-group">
      <label>Product price</label>
      <input type="number" name="pprice">
      </div>

<br><br>
<button type="submit" class="btn" name="Save" >Place order</button>
</form>
</body>
</html>
''')

