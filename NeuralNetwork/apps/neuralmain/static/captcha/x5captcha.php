<?php
include("../res/x5engine.php");
$nameList = array("kg4","yff","dgl","mnx","nma","76m","drr","4t6","mx4","v32");
$charList = array("3","G","7","2","P","G","L","2","R","Y");
$cpt = new X5Captcha($nameList, $charList);
//Check Captcha
if ($_GET["action"] == "check")
	echo $cpt->check($_GET["code"], $_GET["ans"]);
//Show Captcha chars
else if ($_GET["action"] == "show")
	echo $cpt->show($_GET['code']);
// End of file x5captcha.php
