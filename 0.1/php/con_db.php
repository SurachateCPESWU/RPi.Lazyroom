<?php

$Host="";
$User="";
$Pass="";
$dbname = "";

$conn=new mysqli($Host,$User,$Pass,$dbname);

if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

?>