from django.contrib import admin
from .models import Music, Singer, Genre
# Register your models here.
admin.site.register(Music)
admin.site.register(Singer)
admin.site.register(Genre)