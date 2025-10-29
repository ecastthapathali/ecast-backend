from django.contrib import admin
from django.utils.html import format_html
from .models import ArticleForm


@admin.register(ArticleForm)
class ArticleFormAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'theme', 'college_name', 'word_count', 'status_badges', 'filled_date']
    list_filter = ['theme', 'confirmation', 'agreement', 'filled_date', 'college_name']
    search_fields = ['name', 'email', 'title', 'college_name']
    readonly_fields = ['id', 'filled_date', 'file_link']
    date_hierarchy = 'filled_date'
    
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'email', 'phone', 'college_name')
        }),
        ('Article Details', {
            'fields': ('title', 'theme', 'word_count', 'article_file', 'file_link')
        }),
        ('Content', {
            'fields': ('abstract', 'keywords', 'reference'),
            'classes': ('collapse',)
        }),
        ('Questions', {
            'fields': ('question_1', 'question_2'),
            'classes': ('collapse',)
        }),
        ('Status & Agreement', {
            'fields': ('confirmation', 'agreement', 'filled_date', 'id')
        }),
    )
    
    def status_badges(self, obj):
        badges = []
        if obj.confirmation:
            badges.append('<span style="background-color: #28a745; color: white; padding: 3px 8px; border-radius: 3px; margin-right: 5px;">✓ Confirmed</span>')
        if obj.agreement:
            badges.append('<span style="background-color: #007bff; color: white; padding: 3px 8px; border-radius: 3px;">✓ Agreed</span>')
        if not badges:
            badges.append('<span style="background-color: #dc3545; color: white; padding: 3px 8px; border-radius: 3px;">Pending</span>')
        return format_html(''.join(badges))
    status_badges.short_description = 'Status'
    
    def file_link(self, obj):
        if obj.article_file:
            return format_html('<a href="{}" target="_blank">Download Article File</a>', obj.article_file.url)
        return "-"
    file_link.short_description = 'File'