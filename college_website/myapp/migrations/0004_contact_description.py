# Generated by Django 5.0.6 on 2024-06-15 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_rename_user_email_contact_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='Description',
            field=models.TextField(default='Nothings Happens'),
        ),
    ]