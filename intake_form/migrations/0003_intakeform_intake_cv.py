# Generated by Django 4.0 on 2023-06-28 02:39

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('intake_form', '0002_rename_email_intakeform_intake_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='intakeform',
            name='intake_cv',
            field=models.FileField(default=django.utils.timezone.now, upload_to='media/intake_cv/'),
            preserve_default=False,
        ),
    ]