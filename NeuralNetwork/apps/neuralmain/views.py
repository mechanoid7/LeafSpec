import copy
from datetime import datetime

from django.shortcuts import render, redirect
from django.core.files.storage import FileSystemStorage
from .forms import PhotoToDatabaseForm, PhotoRequestForm, ContactsForm, AuthForm
from .admin import auth_data
from .tools.training import retrain_sys


def main(request):
    # BASE_DIR_DATA_REQUESTS = BASE_DIR+"_Data\\requests" - DISABLED
    # current path: media/requests/
    data_to_page = {}

    uploaded_file = None
    file = None
    if request.method == "POST":
        uploaded_file = request.FILES['photo_file']
        # uploaded_file = request.FILES.get('photo_file', False)
        print(str(uploaded_file))
        if not uploaded_file.multiple_chunks(chunk_size=20971520):  # 20 MB
            file = uploaded_file.read()
            fs = FileSystemStorage()
            name = fs.save("requests\\" + uploaded_file.name, uploaded_file)  # BASE_DIR_DATA_REQUESTS+"\\"+
            url = fs.url(name)
            form = PhotoRequestForm(request.POST, request.FILES)
            data_to_page['message'] = "Успешно"
        else:
            form = PhotoRequestForm()
            data_to_page['error'] = "Файл не может быть больше 20мб."
            print("Uploaded file: '"+uploaded_file.name+"' big, not saved")
    else:
        form = PhotoRequestForm()
    data_to_page['form'] = form
    return render(request, "website/main.html", data_to_page)


def upload(request):
    form = {}
    data_to_page = {}
    if request.method == 'POST':
        uploaded_file = request.FILES['photo_file']
        # print(str(uploaded_file))
        if not uploaded_file.multiple_chunks(chunk_size=20971520):  # 20 MB
            x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')  # take ip adress user
            if x_forwarded_for:
                ipaddress = x_forwarded_for.split(',')[-1].strip()
            else:
                ipaddress = request.META.get('REMOTE_ADDR')

            post = copy.deepcopy(request.POST)  # make request copy and change data
            post['photo_author_ip'] = ipaddress  # set ip adress
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
    form = {}
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
    form = {}
    data_to_page = {}
    if request.method == 'POST':
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')  # take ip adress user
        if x_forwarded_for:
            ipaddress = x_forwarded_for.split(',')[-1].strip()
        else:
            ipaddress = request.META.get('REMOTE_ADDR')

        post_copy = copy.deepcopy(request.POST)  # make request copy and change data
        post_copy['author_ip'] = ipaddress  # set ip adress
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
    return render(request, 'website/pattern.html')

