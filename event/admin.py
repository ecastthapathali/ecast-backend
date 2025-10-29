from django.contrib import admin
from django.utils.html import format_html
from .models import Event, Newsletter, Image

# Register your models here.


class ImageInline(admin.TabularInline):
    model = Image
    extra = 1
    fields = ['image', 'image_preview']
    readonly_fields = ['image_preview']
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="100" height="100" style="object-fit: cover;" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Preview'


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'time', 'location', 'featured', 'coming_soon', 'registration_required']
    list_filter = ['featured', 'coming_soon', 'registration_required', 'date']
    search_fields = ['title', 'location', 'description']
    readonly_fields = ['id', 'slug', 'image_preview']
    list_editable = ['featured', 'coming_soon']
    date_hierarchy = 'date'
    inlines = [ImageInline]
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'image', 'image_preview')
        }),
        ('Event Details', {
            'fields': ('date', 'time', 'location', 'contact_email')
        }),
        ('Registration Settings', {
            'fields': ('registration_required', 'registration_deadline', 'max_attendees'),
            'classes': ('collapse',)
        }),
        ('Status', {
            'fields': ('featured', 'coming_soon', 'id')
        }),
    )
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="200" height="150" style="object-fit: cover;" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Image Preview'


@admin.register(Newsletter)
class NewsletterAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'event_name', 'formatted_id']
    search_fields = ['name', 'email', 'for_event__title']
    list_filter = ['for_event']
    readonly_fields = ['id']
    autocomplete_fields = ['for_event']
    
    def event_name(self, obj):
        return obj.for_event.title
    event_name.short_description = 'Event'
    event_name.admin_order_field = 'for_event__title'
    
    def formatted_id(self, obj):
        return str(obj.id)[:8]
    formatted_id.short_description = 'ID'


@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ['event_name', 'image_preview', 'formatted_id']
    list_filter = ['for_event']
    search_fields = ['for_event__title']
    readonly_fields = ['id', 'image_preview']
    autocomplete_fields = ['for_event']
    
    def event_name(self, obj):
        return obj.for_event.title
    event_name.short_description = 'Event'
    event_name.admin_order_field = 'for_event__title'
    
    def formatted_id(self, obj):
        return str(obj.id)[:8]
    formatted_id.short_description = 'ID'
    
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="150" height="150" style="object-fit: cover;" />', obj.image.url)
        return "-"
    image_preview.short_description = 'Preview'
