import copy
import datetime
# import os
# import time

# from django.conf import settings
from django.shortcuts import render, redirect
# from django.http import HttpResponse, HttpResponseRedirect
# from django.urls import reverse_lazy
# from django.views.generic import CreateView
from django.core.files.storage import FileSystemStorage

# from django.views.generic.base import View
from .forms import PhotoToDatabaseForm, PhotoRequestForm
# from .models import PhotoRequest, PhotoToDatabase
# from .img_handler import handle  # функция для обработки изображения
# from .models import PhotoInDatabase
# from NeuralNetwork.settings import BASE_DIR
# from .models import PhotoAnswer


# class MainView(View):  # available links
#     """ Вывод ответа """
#     def get(self, request):
#         photos = PhotoInDatabase.objects.all()
#         # photos = ["123", "456", "789"]
#         # return render(request, "HTML_sites/main.html", {"photos": photos})
#         return render(request, "website/main.html", {"photos": photos})


def auth(request):
    return render(request, 'website/auth.html', {})


def contacts(request):
    return render(request, 'website/contacts.html', {})


def main_user_request(request):
    # BASE_DIR_DATA_REQUESTS = BASE_DIR+"_Data\\requests" - DISABLED
    # current path: media/requests/
    context = {}
    uploaded_file = None
    file = None
    if request.method == "POST":
        uploaded_file = request.FILES['img']
        if not uploaded_file.multiple_chunks(chunk_size=20971520):  # 20 MB
            file = uploaded_file.read()
            fs = FileSystemStorage()
            name = fs.save("requests\\" + uploaded_file.name, uploaded_file)  # BASE_DIR_DATA_REQUESTS+"\\"+
            url = fs.url(name)
            context = {'url': fs.url(name), "path": 225}
        else:
            context['message'] = "Файл не может быть больше 20мб."
            print("Uploaded file:", uploaded_file.name, "big, not saved")

    return render(request, "website/main_upload.html", context)


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


# def main_else(request):
#     data_to_page = {}
#     if request.method == 'POST':
#         post = copy.deepcopy(request.POST)  # make request copy and change data
#         post['photo_date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # set current time
#         post['photo_name'] = post['photo_group'] + '_' + str(post['photo_date'])  # name=group+time
#         request.POST = post  # update request for database
#         form = PhotoToDatabaseForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             # return redirect('upload')  # update page
#     else:
#         form = PhotoRequestForm()
#     data_to_page['form'] = form
#     return render(request, "website/main.html", data_to_page)



# global page_msg
def upload(request):
    form = {}
    data_to_page = {}
    if request.method == 'POST':
        x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')  # take ip adress user
        if x_forwarded_for:
            ipaddress = x_forwarded_for.split(',')[-1].strip()
        else:
            ipaddress = request.META.get('REMOTE_ADDR')
        # print("Ip adress request:", ipaddress)

        post = copy.deepcopy(request.POST)  # make request copy and change data
        post['photo_author_ip'] = ipaddress  # set ip adress
        post['photo_date'] = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # set current time
        post['photo_name'] = post['photo_group']+'_'+str(post['photo_date'])  # name=group+time
        request.POST = post  # update request for database

        form = PhotoToDatabaseForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            data_to_page['message'] = 'Спасибо за помощь проекту.'
            # return redirect('upload')  # update page
    else:
        form = PhotoToDatabaseForm()
    data_to_page['form'] = form
    return render(request, 'website/upload.html', data_to_page)  # {'form': form}


def pattern(request):
    return render(request, 'website/pattern.html')


def thnx(request):
    return render(request, 'website/upload.html', {'message': 'Спасибо за помощь проекту!'})
