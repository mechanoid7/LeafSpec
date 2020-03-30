<?php
if(substr(basename($_SERVER['PHP_SELF']), 0, 11) == "imEmailForm") {
	include '../res/x5engine.php';
	$form = new ImForm();
	$fileResult = $form->setFile('Выберите файл изображения для сканирования:', $_FILES['imObjectForm_3_1'], $imSettings['general']['public_folder'], '', 'jpg, png, jpeg');
	if ($fileResult == -1) { die(imPrintError('Cannot send file: Выберите файл изображения для сканирования:')); }
	if ($fileResult < -1) { die(imPrintError('В поле "Выберите файл изображения для сканирования:" указан неверный формат.')); }

	if(@$_POST['action'] != 'check_answer') {
		if(!isset($_POST['imJsCheck']) || $_POST['imJsCheck'] != 'jsactive' || (isset($_POST['imSpProt']) && $_POST['imSpProt'] != ""))
			die(imPrintJsError());
		$form->mailToOwner('database@mechanoid.db', 'database@mechanoid.db', '', '', false);
		@header('Location: ../index.html');
		exit();
	} else {
		echo $form->checkAnswer(@$_POST['id'], @$_POST['answer']) ? 1 : 0;
	}
}

// End of file