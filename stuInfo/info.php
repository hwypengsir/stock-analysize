<html>
<head>
        <meta charset="UTF-8">
        <title></title>

        <style type="text/css">
            div{margin:20px  auto;text-align:center;}
        </style>
</head>

<body>
<?php

$hostname='localhost';
$dbname='stuInfo';
$username='root';
$password='xyzzy';

$major=$_POST['major'];
$name=$_POST['name'];
$sexulity=$_POST['sexulity'];
$locality=$_POST['locality'];
$readingway=$_POST['readingway'];
$pid=$_POST['pid'];
$phone=$_POST['phone'];
$email=$_POST['email'];
$fname=$_POST['fname'];
$fphone=$_POST['fphone'];
$mname=$_POST['mname'];
$mphone=$_POST['mphone'];
$kname=$_POST['kname'];
$kphone=$_POST['kphone'];

try {
    $conn = new PDO("mysql:host=$hostname;dbname=$dbname", $username, $password);
    // set the PDO error mode to exception
    $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION);
    $sql = "INSERT INTO stuInfo (major,name,sexulity,locality,readingway,pid,phone,email,fname,fphone,mname,mphone,kname,kphone)".
           "VALUES (:major,:name,:sexulity,:locality,:readingway,:pid,:phone,:email,:fname,:fphone,:mname,:mphone,:kname,:kphone)";

    $statement=$conn->prepare($sql);
    $statement->execute(array(':major'=> $major,':name'=> $name,':sexulity'=> $sexulity,':locality'=> $locality,':readingway'=> $readingway,
                              ':pid'=> $pid,':phone'=> $phone,':email'=> $email,':fname'=> $fname,':fphone'=> $fphone,
                              ':mname'=> $mname,':mphone'=> $mphone,':kname'=> $kname,':kphone'=> $kphone));
    }
catch(PDOException $e)
    {
    echo $sql . "<br>" . $e->getMessage();
    }

$conn = null;

?>
<div>
<img src="logo.jpeg">
<p>海外院国际商务系欢迎您</p>
<?php  echo $name?> 的个人信息已经成功收集</br>
祝学习生活愉快 
</div>

</body>
</html>
