from django.contrib import admin
from .models import PhotoRequest, PhotoInDatabase, PhotoToDatabase, PhotoAnswer
# Register your models here.

admin.site.register(PhotoRequest)
admin.site.register(PhotoInDatabase)
admin.site.register(PhotoToDatabase)
admin.site.register(PhotoAnswer)


