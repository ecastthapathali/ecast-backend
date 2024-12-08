from django.contrib import admin
from .models import ParticipationCertificate
from .models import generate_random_uid

@admin.register(ParticipationCertificate)
class ParticipationCertificateAdmin(admin.ModelAdmin):
    list_display = ('name', 'event_name', 'date', 'custom_id')
    search_fields = ('name', 'event_name')

    def save_model(self, request, obj, form, change):
        if not obj.custom_id:
            obj.custom_id = generate_random_uid() 
        super().save_model(request, obj, form, change)
