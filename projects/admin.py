from django.contrib import admin
from django.utils.html import format_html
from .models import Project

# Register your models here.


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'featured', 'has_live_link', 'image_preview', 'formatted_id']
    list_filter = ['featured']
    search_fields = ['title', 'description', 'repo_link']
    readonly_fields = ['id', 'image_preview']
    list_editable = ['featured']
    actions = ['mark_as_featured', 'mark_as_not_featured']
    list_per_page = 20
    
    fieldsets = (
        ('Project Information', {
            'fields': ('title', 'description', 'image', 'image_preview')
        }),
        ('Links', {
            'fields': ('repo_link', 'live_link')
        }),
        ('Settings', {
            'fields': ('featured', 'id')
        }),
    )
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="200" height="150" style="object-fit: cover;" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Image Preview'
    
    def has_live_link(self, obj):
        if obj.live_link:
            return format_html('<span style="color: green;">✓</span>')
        return format_html('<span style="color: red;">✗</span>')
    has_live_link.short_description = 'Live'
    
    def formatted_id(self, obj):
        return str(obj.id)[:8]
    formatted_id.short_description = 'ID'
    
    def mark_as_featured(self, request, queryset):
        """Mark selected projects as featured"""
        updated = queryset.update(featured=True)
        self.message_user(request, f'{updated} project(s) marked as featured.')
    mark_as_featured.short_description = "⭐ Mark as Featured"
    
    def mark_as_not_featured(self, request, queryset):
        """Remove featured status from selected projects"""
        updated = queryset.update(featured=False)
        self.message_user(request, f'{updated} project(s) unmarked as featured.')
    mark_as_not_featured.short_description = "☆ Remove Featured"