from django.contrib import admin
from intake_form.models import IntakeForm
# Register your models here.


class IntakeAdmin(admin.ModelAdmin):
    list_display = ('intake_name', 'intake_rollno', 'intake_email', 'intake_position')

admin.site.register(IntakeForm, IntakeAdmin)