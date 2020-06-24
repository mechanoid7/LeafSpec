"""NeuralMain app logic. Each function is responsible for one page."""
import copy
from datetime import datetime

from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .forms import PhotoToDatabaseForm, PhotoRequestForm, ContactsForm, AuthForm
from .admin import auth_data
from .tools.training import retrain_sys
from .tools.analyze_img import detect_image
from .tools.file_manipulator import check_file_name, check_filename_extension, delete_file


def main(request):
    """ Function main page. Process uploaded image and defines a type of plant. And save request object to DB.
    Object of PhotoRequest(see item neuralmain/models)
    Parameters:
        - :data_to_page: data that is sent to the page for output to the user (Error/success msg. Success mgs have info about type of plant(-s).)
        - :uploaded_file: user img file

    Returns:
        - :data_to_page(list): error or image plant information.
    """
    # BASE_DIR_DATA_REQUESTS = BASE_DIR+"_Data\\requests" - DISABLED
    # current path: media/requests/
    data_to_page = {}

    uploaded_file = None
    if request.method == "POST":
        uploaded_file = request.FILES['photo_file']
        # uploaded_file = request.FILES.get('photo_file', False)
        # print(str(uploaded_file))
        if not uploaded_file.multiple_chunks(chunk_size=20971520):  # 20 MB
            fs = FileSystemStorage()

            uploaded_file.name = check_file_name(uploaded_file.name)
            name = fs.save("requests\\" + uploaded_file.name, uploaded_file)  # BASE_DIR_DATA_REQUESTS+"\\"+
            url = fs.url(name)
            form = PhotoRequestForm(request.POST, request.FILES)

            if check_filename_extension(uploaded_file.name):
                data_to_page['error'] = 'Неверный формат файла.'
            else:
                try:
                    data_to_page['message'] = detect_image(url)
                except Exception:
                    data_to_page['error'] = 'Невозможно распознать файл, Файл повреждён или неизвестен.'
                    delete_file(url)

        else:
            form = PhotoRequestForm()
            data_to_page['error'] = "Файл не может быть больше 20мб."
            print(f"Uploaded file: '{uploaded_file.name}' big, not saved")
    else:
        form = PhotoRequestForm()
    data_to_page['form'] = form
    return render(request, "website/main.html", data_to_page)


def upload(request):
    """ Function upload page. Save upload object to DB.
    Object of PhotoToDatabase(see item neuralmain/models)
    Parameters:
        - :uploaded_file(file): user img file
        - :data_to_page(list): data that is sent to the page for output to the user (Error/success msg. Success mgs have success text.)

    Returns:
        - :data_to_page(list): error or success message.
    """
    data_to_page = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['photo_file']
        # print(str(uploaded_file))
        if not uploaded_file.multiple_chunks(chunk_size=20971520):  # 20 MB
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')  # take ip address user
            if x_forwarded_for:
                ipaddress = x_forwarded_for.split(',')[-1].strip()
            else:
                ipaddress = request.META.get('REMOTE_ADDR')

            post = copy.deepcopy(request.POST)  # make request copy and change data
            post['photo_author_ip'] = ipaddress  # set ip address
            post['photo_date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # set current time
            post['photo_name'] = uploaded_file.name  # name=group+time
            request.POST = copy.deepcopy(post)  # update request for database

            form = PhotoToDatabaseForm(request.POST, request.FILES)
            if form.is_valid():
                form.save()
                data_to_page['message'] = 'Спасибо за помощь проекту.'
                # return redirect('upload')  # update page
        else:
            form = PhotoToDatabaseForm(request.POST, request.FILES)
            data_to_page['error'] = 'Big file'
    else:
        form = PhotoToDatabaseForm()
    data_to_page['form'] = form
    return render(request, 'website/upload.html', data_to_page)  # {'form': form}


def auth(request):
    """ Function auth page. Gives access to start relearn system. If login and password field is correct - show button to relearn.
    Object of Auth(see item neuralmain/models)
    Parameters:
        - :data_to_page: data that is sent to the page for output to the user (Error/success msg. Success mgs have success text.)

    Returns:
        - :data_to_page(list):login error or site access.
    """
    data_to_page = {}
    if request.method == 'POST':
        form = AuthForm(request.POST)
        if form.is_valid():
            login = request.POST['login_field']  # запись логина и пароля в переменные
            password = request.POST['password_field']
            if login in auth_data and password == auth_data[login]:  # если есть логин в списке и пароль к нему правильные - пользователь получает допуск
                #easteregg
                data_to_page['access'] = True
                if login == 'mechanoid':  # особое сообщение для меня :3
                    data_to_page['message'] = 'Привет, хозяин!'
                else:
                    data_to_page['message'] = 'Добро пожаловать на Leaf Spectator!'
                print(f">>> User '{login}' logged in to the site.")
            else:
                data_to_page['error'] = 'Неверный логин или пароль.'
        else:
            if request.POST['access_field'].lower() == 'подтвердить':
                answer_args = retrain_sys()  # вызов функции переобучения нейросети
                if answer_args[0]:
                    data_to_page['message'] = 'Успешно, нейросеть переобучается. Это займёт некоторое время.'
                else:
                    data_to_page['error'] = f'Тренировку системы можно будет запустить через {answer_args[1]:.2f} часа(-ов).'

            else:
                data_to_page['error'] = 'Fatal Error, contact us to solve the problem.'
                form = AuthForm(request.POST)
    else:
        form = AuthForm()
    data_to_page['form'] = form
    return render(request, 'website/auth.html', data_to_page)  # {'form': form}


def contacts(request):
    """ Function Contacts page. Ability to communicate with the administrator / moderator. If the fields  are valid - save letter to DB.
    Object of Contacts(see item neuralmain/models)
    Parameters:
        - :data_to_page(list): data that is sent to the page for output to the user (Error/success msg. Success mgs have success text.)

    Returns:
        :data_to_page(list):error or success message.
    """
    data_to_page = {}
    if request.method == 'POST':
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')  # take ip address user
        if x_forwarded_for:
            ipaddress = x_forwarded_for.split(',')[-1].strip()
        else:
            ipaddress = request.META.get('REMOTE_ADDR')

        post_copy = copy.deepcopy(request.POST)  # make request copy and change data
        post_copy['author_ip'] = ipaddress  # set ip address
        request.POST = copy.deepcopy(post_copy)  # update request for database

        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            data_to_page['message'] = 'Спасибо за Ваше обращение.'
            # return redirect('upload')  # update page
        else:
            form = ContactsForm(request.POST)
            data_to_page['error'] = 'Big file'
    else:
        form = ContactsForm()
    data_to_page['form'] = form
    return render(request, 'website/contacts.html', data_to_page)  # {'form': form}


def pattern(request):
    """ Function pattern page. If current mode is Debug: load clear pattern page. """
    return render(request, 'website_new/pattern.html')

