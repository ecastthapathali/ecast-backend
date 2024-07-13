from django.contrib import admin
from .models import ContentForm


@admin.register(ContentForm)
class ContentFormAdmin(admin.ModelAdmin):
    list_display = ["name","roll_number","email","phone"]
