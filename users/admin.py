from django.contrib import admin

from .models import Stopien, Kierunek, Wydzial, User

# Register your models here.

admin.site.register([Stopien, Kierunek, Wydzial, User])
