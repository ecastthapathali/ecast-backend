from django.contrib import admin
from django.utils.html import format_html
from .models import ParticipationCertificate, generate_random_uid


@admin.register(ParticipationCertificate)
class ParticipationCertificateAdmin(admin.ModelAdmin):
    list_display = ['name', 'event_name', 'date', 'custom_id_short', 'generated_at']
    search_fields = ['name', 'event_name', 'custom_id']
    list_filter = ['date', 'generated_at']
    readonly_fields = ['custom_id', 'generated_at', 'certificate_url']
    date_hierarchy = 'date'
    
    fieldsets = (
        ('Participant Information', {
            'fields': ('name', 'event_name', 'date')
        }),
        ('Certificate Details', {
            'fields': ('custom_id', 'certificate_url', 'generated_at')
        }),
    )
    
    def custom_id_short(self, obj):
        return format_html('<code style="background-color: #f4f4f4; padding: 2px 6px; border-radius: 3px;">{}</code>', obj.custom_id[:20] + '...' if len(obj.custom_id) > 20 else obj.custom_id)
    custom_id_short.short_description = 'Certificate ID'
    
    def certificate_url(self, obj):
        if obj.custom_id:
            url = f'/certificates/{obj.custom_id}/'
            return format_html('<a href="{}" target="_blank">{}</a>', url, url)
        return "-"
    certificate_url.short_description = 'Certificate URL'
    
    def save_model(self, request, obj, form, change):
        if not obj.custom_id:
            obj.custom_id = generate_random_uid() 
        super().save_model(request, obj, form, change)
