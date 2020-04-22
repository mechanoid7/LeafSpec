запустить git bash, каталог - cd /F/Projects/PyCharm/NeuralNetwork

	git init - инициация нового репозитория
	git add . - добавить все файлы в текущем каталоге 
	
echo "# LeafSpec" >> README.md
git init
git add README.md
git commit -m "first commit"
git remote add origin https://github.com/mechanoid7/LeafSpec.git
git push -u origin master



	 Удалить из отслеживания папку: git rm -r --cached NeuralNetwork/apps/neuralmain/bin/
