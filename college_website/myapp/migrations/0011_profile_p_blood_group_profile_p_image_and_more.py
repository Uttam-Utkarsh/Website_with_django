# Generated by Django 5.0.6 on 2024-07-04 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_alter_notice_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='P_Blood_group',
            field=models.CharField(default='none', max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='P_Image',
            field=models.ImageField(default='none', upload_to='Profile_image'),
        ),
        migrations.AddField(
            model_name='profile',
            name='P_PhoneNo',
            field=models.CharField(default='none', max_length=20),
        ),
        migrations.AddField(
            model_name='profile',
            name='P_Rollno',
            field=models.CharField(default='none', max_length=10),
        ),
        migrations.AddField(
            model_name='profile',
            name='P_Subject',
            field=models.CharField(default='none', max_length=20),
        ),
        migrations.AlterField(
            model_name='profile',
            name='P_Email',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='P_Name',
            field=models.CharField(default='none', max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='P_Password',
            field=models.CharField(default='none', max_length=100),
        ),
    ]