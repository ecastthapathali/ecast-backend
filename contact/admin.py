from django.contrib import admin
from django.utils.html import format_html
from django.http import HttpResponse
import csv
from .models import ContactForm


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message_preview', 'submitted_at']
    list_filter = ['submitted_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['id', 'name', 'email', 'message', 'submitted_at']
    date_hierarchy = 'submitted_at'
    actions = ['export_to_csv']
    list_per_page = 30
    
    fieldsets = (
        ('Contact Information', {
            'fields': ('name', 'email')
        }),
        ('Message', {
            'fields': ('message',)
        }),
        ('System', {
            'fields': ('submitted_at', 'id'),
            'classes': ('collapse',)
        }),
    )
    
    def message_preview(self, obj):
        if len(obj.message) > 50:
            return obj.message[:50] + '...'
        return obj.message
    message_preview.short_description = 'Message Preview'
    
    def has_add_permission(self, request):
        # Don't allow adding contact forms from admin
        return False
    
    def has_delete_permission(self, request, obj=None):
        # Allow deletion but not addition
        return True
    
    def export_to_csv(self, request, queryset):
        """Export selected contact messages to CSV"""
        field_names = ['name', 'email', 'message', 'submitted_at']
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename=contact_messages.csv'
        writer = csv.writer(response)
        
        # Write headers
        writer.writerow(field_names)
        
        # Write data
        for obj in queryset:
            writer.writerow([getattr(obj, field) for field in field_names])
        
        return response
    
    export_to_csv.short_description = "📥 Export selected to CSV"
