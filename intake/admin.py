from django.contrib import admin
from django.utils.html import format_html
from .models import IntakeForm


@admin.register(IntakeForm)
class IntakeFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'campus_roll', 'department', 'batch', 'post', 'social_links', 'filled_date']
    list_filter = ['post', 'department', 'batch', 'filled_date']
    search_fields = ['name', 'email', 'campus_roll']
    readonly_fields = ['id', 'filled_date', 'resume_link']
    date_hierarchy = 'filled_date'
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'email', 'phone', 'campus_roll')
        }),
        ('Academic Details', {
            'fields': ('department', 'batch')
        }),
        ('Application', {
            'fields': ('post', 'about', 'reason_to_join', 'interests')
        }),
        ('Documents', {
            'fields': ('resume', 'resume_link')
        }),
        ('Social Media', {
            'fields': ('github_link', 'linkedin_link', 'facebook_link'),
            'classes': ('collapse',)
        }),
        ('System', {
            'fields': ('filled_date', 'id'),
            'classes': ('collapse',)
        }),
    )
    
    def social_links(self, obj):
        links = []
        if obj.github_link:
            links.append('<span style="background-color: #333; color: white; padding: 2px 6px; border-radius: 3px; margin-right: 3px;">GitHub</span>')
        if obj.linkedin_link:
            links.append('<span style="background-color: #0077b5; color: white; padding: 2px 6px; border-radius: 3px; margin-right: 3px;">LinkedIn</span>')
        if obj.facebook_link:
            links.append('<span style="background-color: #1877f2; color: white; padding: 2px 6px; border-radius: 3px;">Facebook</span>')
        if not links:
            return "-"
        return format_html(''.join(links))
    social_links.short_description = 'Social Media'
    
    def resume_link(self, obj):
        if obj.resume:
            return format_html('<a href="{}" target="_blank">Download Resume</a>', obj.resume.url)
        return "-"
    resume_link.short_description = 'Resume File'