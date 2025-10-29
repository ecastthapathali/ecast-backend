from django.contrib import admin
from django.utils.html import format_html
from .models import ContactForm


@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'message_preview', 'submitted_at']
    list_filter = ['submitted_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['id', 'name', 'email', 'message', 'submitted_at']
    date_hierarchy = 'submitted_at'
    
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
