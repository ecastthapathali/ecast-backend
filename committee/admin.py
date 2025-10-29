from django.contrib import admin
from django.utils.html import format_html
from .models import CommitteeMember, SocialMedia


class SocialMediaInline(admin.TabularInline):
    model = SocialMedia
    extra = 1
    fields = ['platform', 'handle']


@admin.register(CommitteeMember)
class CommitteeMemberAdmin(admin.ModelAdmin):
    inlines = [SocialMediaInline]
    list_display = ['name', 'position', 'tenure', 'started_from', 'photo_preview']
    list_filter = ['position', 'started_from', 'tenure']
    search_fields = ['name', 'position']
    readonly_fields = ['id', 'photo_preview']
    date_hierarchy = 'started_from'
    
    fieldsets = (
        ('Member Information', {
            'fields': ('name', 'position')
        }),
        ('Tenure Details', {
            'fields': ('started_from', 'tenure')
        }),
        ('Photo', {
            'fields': ('memberPhoto', 'photo_preview')
        }),
        ('System', {
            'fields': ('id',),
            'classes': ('collapse',)
        }),
    )
    
    def photo_preview(self, obj):
        if obj.memberPhoto:
            return format_html('<img src="{}" width="100" height="100" style="object-fit: cover; border-radius: 50%;" />', obj.memberPhoto)
        return "-"
    photo_preview.short_description = 'Photo'


@admin.register(SocialMedia)
class SocialMediaAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'platform', 'handle_link']
    list_filter = ['platform', 'user']
    search_fields = ['user__name', 'platform']
    autocomplete_fields = ['user']
    
    fieldsets = (
        ('Social Media Details', {
            'fields': ('user', 'platform', 'handle')
        }),
    )
    
    def user_name(self, obj):
        return obj.user.name
    user_name.short_description = 'Member'
    user_name.admin_order_field = 'user__name'
    
    def handle_link(self, obj):
        return format_html('<a href="{}" target="_blank">{}</a>', obj.handle, obj.handle[:50])
    handle_link.short_description = 'Link'

