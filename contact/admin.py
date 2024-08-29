from django.contrib import admin
from .models import ContactForm

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "submitted_at"]
    list_filter = ["submitted_at"]

admin.site.register(ContactForm, ContactFormAdmin)
