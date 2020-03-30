<?php
if(substr(basename($_SERVER['PHP_SELF']), 0, 11) == "imEmailForm") {
	include '../res/x5engine.php';
	$form = new ImForm();
	$form->setField('Автор:', $_POST['imObjectForm_1_1'], '', false);
	$form->setField('Название растения:', $_POST['imObjectForm_1_2'], '', false);
	$fileResult = $form->setFile('Загрузите файл фотографии:', $_FILES['imObjectForm_1_3'], $imSettings['general']['public_folder'], '', 'jpg, jpeg, png, gif');
	if ($fileResult == -1) { die(imPrintError('Cannot send file: Загрузите файл фотографии:')); }
	if ($fileResult < -1) { die(imPrintError('В поле "Загрузите файл фотографии:" указан неверный формат.')); }

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