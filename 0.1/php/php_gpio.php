<html>
<link rel = "stylesheet" type = "text/css" href = "css/style.css" >
<?php

function GET_PIN($Dv_name)
{
	include("con_db.php");
	$temp="'".$Dv_name."'";
	$sql = "SELECT `Pin` FROM `DEVICE` WHERE Name=$temp";
	$result = $conn->query($sql);
	if ($result->num_rows > 0) 
	{
    while($row = $result->fetch_assoc()) 
    {
        return $row[Pin];
    }
	}
}

function Check($Dv_name)
{
	include("con_db.php");
	$temp="'".$Dv_name."'";
	$sql = "SELECT * FROM `DEVICE` WHERE Name=$temp";
	$result = $conn->query($sql);
	if ($result->num_rows > 0) 
	{
    while($row = $result->fetch_assoc()) 
    {
        return $row[Status];
    }
	}
}

function TURN_ON($Dv_name)
{
	$Pin=GET_PIN("$Dv_name");
	exec("gpio write $Pin 0");
	include("con_db.php");
	$temp="'".$Dv_name."'";
	$sql = "UPDATE `DEVICE` SET `Status` =1 WHERE Name = $temp";
	$result = $conn->query($sql);
	echo "$Dv_name is on."."<br>";
}

function TURN_OFF($Dv_name)
{
	$Pin=GET_PIN("$Dv_name");
	exec("gpio write $Pin 1");
	include("con_db.php");
	$temp="'".$Dv_name."'";
	$sql = "UPDATE `DEVICE` SET `Status` =0 WHERE Name = $temp";
	$result = $conn->query($sql);
	echo "$Dv_name is off."."<br>";
}

  if (isset($_GET['ON'])) 
  {
  	$Status=Check($_GET['ON']);
  	if ($Status==0) {
  		TURN_ON($_GET['ON']);
  	}
  	elseif ($Status==1) {
  		echo "Error"."<br>";
  	}
  }
  elseif (isset($_GET['OFF'])) 
  {
  	$Status=Check($_GET['OFF']);
  	if ($Status==1) {
  		TURN_OFF($_GET['OFF']);
  	}
  	elseif ($Status==0) {
  		echo "Error"."<br>";
  	}
  }

$i=1;
while ( $i <= 4) 
{
	?>
	<a>Device <?php echo $i;?>  </a><a href='php_gpio.php?ON=DEVICE<?php echo $i;?>'>ON</a>
	<a href='php_gpio.php?OFF=DEVICE<?php echo $i;?>'>OFF</a>
	<br>
	<?php
	$i++;
}
?>
</html>