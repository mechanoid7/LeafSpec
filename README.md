# LeafSpec
### Нейросеть для распознавания листьев растений

Используется язык программирования Python.
Планируется использовать библиотеку для нейросетей TensorFlow.

Создано веб-приложение с серверной частью. 
Веб-приложение имеет 4 страницы(Главная, для загрузки фото в БД, Авторизация, Контакты). 

* На главной странице можно загрузить фото для последующей обработки и распознавания нейронной сетью.
* На странице для выгрузки фото есть поля для заполнения БД: Имя автора, Вид растения, Файл изображения. Имя файла, дата+время, ip-адрес заполняются автоматически системой.
* Страница авторизации не выполняет никакой функции.
* Страница с контактами в стадии модернизации и перехода к управлению Django.

После n-ного количества загруженных и проверенных изображений система запустит переобучение нейросети с учётом новых изображений.

Загруженные фото пользователей помещаются в папку /media/requests/ и /media/image_to_database/, папка будет определяться самой системой с доверительной вероятностью >40% (опционально), после чего будет осуществлена проверка модератором и в случае совпадения помещена в папку с этим видом растения.

| Что планируется сделать                                      | В разработке                                          | Сделано                                                      |
| ------------------------------------------------------------ | ----------------------------------------------------- | ------------------------------------------------------------ |
| Автоматическое обучение системы по какому-либо триггеру(Новое количество фото/разница времени) | "Мозг" системы, обработчик системы на базе TensorFlow | Оболочка сервиса - Сайт(Leaf Spectator)                      |
| Перемещение загруженного изображения(из Главной страницы) в рабочую папку, для дальнейшего распознавания |                                                       | Главная страница, которая позволяет загрузить изображение на сервис для дальнейшей обработки. |
| Переход с TensorFlow 1.4.0 до версии 2.1.0                   |                                                       | Страница для выгрузки изображения, вид которого уже известен, для дальнейшего добавления в базу, после проверки модератором. |
| Обработчик полученных сообщений из страницы "Контакты"       |                                                       | Страница авторизации с готовыми полями.                      |
| Отладка реакции сервиса на попытку авторизации на странице Авторизации. |                                                       | Страница "Контакты" для связи с разработчиком/модератором, добавление e-mail адресов и сообщений в БД. Настроено поле для e-mail адреса. |


#### Примечание
- В папке 'examples' содержится вид страниц сайта.

