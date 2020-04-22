from django.contrib import admin
from .models import PhotoRequest, PhotoToDatabase
# from os import subprocess
# import os
# import pathlib
# import datetime
# Register your models here.

admin.site.register(PhotoRequest)
# admin.site.register(PhotoInDatabase)
admin.site.register(PhotoToDatabase)
# admin.site.register(PhotoAnswer)

auth_data = {
    'mechanoid': 'mechanoid',
    'user': 'user32',
    'opg_gremlin': 'iliuha'
}
