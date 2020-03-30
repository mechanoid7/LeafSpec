<?php
if(substr(basename($_SERVER['PHP_SELF']), 0, 11) == "imEmailForm") {
	include '../res/x5engine.php';
	$form = new ImForm();
	$form->setField('Введите ваш e-mail:', $_POST['imObjectForm_1_1'], '', false);
	$form->setField('Введите сообщение:', $_POST['imObjectForm_1_2'], '', false);
	$form->setField('Причина:', $_POST['imObjectForm_1_3'], '', false);

	if(@$_POST['action'] != 'check_answer') {
		if(!isset($_POST['imJsCheck']) || $_POST['imJsCheck'] != 'jsactive' || (isset($_POST['imSpProt']) && $_POST['imSpProt'] != ""))
			die(imPrintJsError());
		$form->mailToOwner($_POST['imObjectForm_1_1'] != "" ? $_POST['imObjectForm_1_1'] : 'leafspectator@gmail.com', 'leafspectator@gmail.com', '', '', false);
		@header('Location: ../index.html');
		exit();
	} else {
		echo $form->checkAnswer(@$_POST['id'], @$_POST['answer']) ? 1 : 0;
	}
}

// End of file