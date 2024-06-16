# Generated by Django 5.0.6 on 2024-06-16 05:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_contact_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Email', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Profile Table',
            },
        ),
    ]