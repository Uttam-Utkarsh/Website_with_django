# Generated by Django 5.0.6 on 2024-06-15 17:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_rename_email_contact_user_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='user_email',
            new_name='Email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='user_name',
            new_name='Name',
        ),
    ]
