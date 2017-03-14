from django.contrib import admin

from .models import Stopien, Kierunek, Wydzial, User


class UserAdmin(admin.ModelAdmin):
	search_fields = ['userID']

#list_display = ['','']

admin.site.register(User, UserAdmin)

admin.site.register([Stopien, Kierunek, Wydzial])
