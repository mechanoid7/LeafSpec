from django.contrib import admin
from .models import Photo, PhotoInDatabase, PhotoToDatabase, PhotoAnswer
# Register your models here.

admin.site.register(Photo)
admin.site.register(PhotoInDatabase)
admin.site.register(PhotoToDatabase)
admin.site.register(PhotoAnswer)


