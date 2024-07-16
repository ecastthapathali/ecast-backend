from django.contrib import admin
from .models import ArticleForm


class ArticleFormAdmin(admin.ModelAdmin):
    list_display = ["name", "college_name", "title"]
    list_filter = ["name", "college_name", "theme"]



admin.site.register(ArticleForm, ArticleFormAdmin)