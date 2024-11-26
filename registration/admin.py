from django.contrib import admin
from .models import RegistrationForm


class RegistrationFormAdmin(admin.ModelAdmin):
    list_display = ["name", "campus_roll", "email"]



admin.site.register(RegistrationForm, RegistrationFormAdmin)