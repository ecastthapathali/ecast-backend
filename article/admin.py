from django.contrib import admin
from .models import ArticleForm


class ArticleFormAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "college_name"]
    list_filter = ["name", "college_name"]



admin.site.register(ArticleForm, ArticleFormAdmin)