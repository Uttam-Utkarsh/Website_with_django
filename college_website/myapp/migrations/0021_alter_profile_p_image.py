# Generated by Django 5.0.6 on 2024-07-06 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0020_alter_profile_p_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='P_Image',
            field=models.ImageField(default='', upload_to='Profile_image/'),
        ),
    ]
