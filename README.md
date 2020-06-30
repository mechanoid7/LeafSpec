# LeafSpec
### Нейросеть для распознавания листьев растений

Используется язык программирования Python.
Планируется использовать библиотеку для нейросетей TensorFlow.

Создано веб-приложение с серверной частью. 
Веб-приложение имеет 4 страницы(Главная, для загрузки фото в БД, Авторизация, Контакты). 

* На главной странице можно загрузить фото для последующей обработки и распознавания нейронной сетью.
* На странице для выгрузки фото есть поля для заполнения БД: Имя автора, Вид растения, Файл изображения. Имя файла, дата+время, ip-адрес заполняются автоматически системой.
* Страница авторизации даёт возможность авторизоваться и запустить переобучение нейронной сети.
* Страница с контактами даёт возможность связаться с модераторами, запрос будет сохранён в БД.

После n-ного количества загруженных и проверенных изображений система запустит переобучение нейросети с учётом новых изображений.

Схема сайта:  
![alt-текст](https://github.com/mechanoid7/LeafSpec_edu/blob/master/examples/img/SiteShema.png "Shema LeafSpec")

Загруженные фото пользователей помещаются в папку /media/requests/ и /media/image_to_database/, папка будет определяться самой системой с доверительной вероятностью >60% (опционально), после чего будет осуществлена проверка модератором и в случае совпадения помещена в папку с этим видом растения.

**Полная и подробная документация  доступна по ссылке "Docs-1", по ссылке "Docs-2" в папке "tools" неполная версия в виде сайта с возможностью поиска.**

| Что планируется сделать                                      | В разработке                                           | Сделано                                                      | Отклонено                                                    |
| :----------------------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| Автоматическое обучение системы по какому-либо триггеру(Новое количество фото/разница времени) | "Мозг" системы, обработчик системы на базе TensorFlow. | Оболочка сервиса - Сайт(Leaf Spectator)                      | Отказ от использования файла '*.ps1' для переобучения системы. |
| Обработчик полученных сообщений из страницы "Контакты"       | Заполнение БД новыми видами растений.                  | Главная страница, которая позволяет загрузить изображение на сервис для дальнейшей обработки. | Перемещение загруженного изображения(из Главной страницы) в рабочую папку, для дальнейшего распознавания |
| Переход с TensorFlow 1.4.0 до версии 2.1.0                   | Оптимизировать сайт для телефонов.                     | Страница для выгрузки изображения, вид которого уже известен, для дальнейшего добавления в базу, после проверки модератором. | Исправление бага, связанного с невозможностью открыть меню в режиме мобильного устройства. |
| Запускать обнаружение в новом потоке(thread)                 |                                                        | Страница авторизации с готовыми полями. Реакция системы на ввод правильного/неправильного логина/пароля. |                                                              |
|                                                              |                                                        | Страница "Контакты" для связи с разработчиком/модератором, добавление e-mail адресов и сообщений в БД. Настроено поле для e-mail адреса. |                                                              |
|                                                              |                                                        | Готовая к использованию и протестированная нейросеть на базе TensorFlow 1.4.0 |                                                              |
|                                                              |                                                        | Ограничение размера выгруженного файла(20мб) на сервер, на обеих страницах. |                                                              |
|                                                              |                                                        | 38 видов растений для обучения нейросети.                    |                                                              |
|                                                              |                                                        | Возможность через страницу авторизации запустить переобучение системы. |                                                              |
|                                                              |                                                        | Блокировка частого переобучения системы. Через сайт систему можно переобучать не чаще 1 раза в 5 часов. |                                                              |
|                                                              |                                                        | Вывод результатов работы системы на главной странице,  русифицированный вывод. Вывод адаптивный. |                                                              |
|                                                              |                                                        | Если после проверки изображения совпадение составляет больше 60% - файл автоматически добавляется в папку с соответствующим названием для последующей проверки. |                                                              |
|                                                              |                                                        | Добавлена защита от выгрузки исполняемых файлов.(Главная страница) |                                                              |
|                                                              |                                                        | Исправлен баг при анализе изображения с названием на кириллице.(Вылет TensorFlow) |                                                              |
|                                                              |                                                        | Исправлен баг с вылетом при загрузке файла, которого невозможно обработать. |                                                              |
|                                                              |                                                        | Необработанные файлы не сохраняются.                         |                                                              |
|                                                              |                                                        | Полная документация проекта.                                 |                                                              |
|                                                              |                                                        | Создан новый сайт.                                           |                                                              |
|                                                              |                                                        | На странице "Контакты" добавлено поле с Темой, поле сохраняется в БД |                                                              |
|                                                              |                                                        | Для страницы выгрузки фото в БД повторен анализ файлов, как на Главной странице, файл сохраняется в папку с названием вида, которые определила система с вложенной папкой с именем пользовательского вида. Если система не определила вид, тогда фото помещается в папку "unknown" |                                                              |

ER-Diagram:  
![alt-текст](https://github.com/mechanoid7/LeafSpec_edu/blob/master/examples/img/ER.png "ER-Diagram LeafSpec")

#### Примечание
- В папке 'examples' содержится вид страниц сайта.



#### Авторы:

- Идея

- Дизайн, вёрстка

- Создание проекта под Django

- Models, Views, Forms Django

- Набор БД для нейросети

- Нейросеть под TensorFlow 1.4.0

- Настройка и обучение нейросети

  ## 		<u>Никита (Mechanoid) Востриков

  







​	 

