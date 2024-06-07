from django.contrib import admin
from .models import IntakeForm


class IntakeFormAdmin(admin.ModelAdmin):
    list_display = ["name", "campus_roll", "post", "email"]
    list_filter = ["post"]



admin.site.register(IntakeForm, IntakeFormAdmin)