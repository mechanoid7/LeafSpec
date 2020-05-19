"""Admin panel settings and root const"""
from django.contrib import admin
from .models import PhotoRequest, PhotoToDatabase, Auth, Contacts


admin.site.register(PhotoRequest)
admin.site.register(PhotoToDatabase)
admin.site.register(Auth)
admin.site.register(Contacts)

auth_data = {
    'mechanoid': 'mechanoid',
    'user': 'user32',
    'opg_gremlin': 'iliuha'
}
