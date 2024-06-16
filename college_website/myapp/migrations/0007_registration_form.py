# Generated by Django 5.0.6 on 2024-06-16 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0006_rename_email_profile_p_email_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration_form',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_first_name', models.CharField(max_length=10)),
                ('student_last_name', models.CharField(max_length=10)),
                ('student_date_of_birth', models.DateField(max_length=8)),
                ('student_email', models.EmailField(max_length=30)),
                ('student_phonenumber', models.CharField(max_length=15)),
                ('student_gender', models.CharField(max_length=10)),
                ('student_address', models.CharField(max_length=100)),
                ('student_city', models.CharField(max_length=10)),
                ('student_pincode', models.CharField(max_length=6)),
                ('student_state', models.CharField(max_length=10)),
                ('student_country', models.CharField(max_length=10)),
                ('student_hobbies', models.CharField(max_length=10)),
                ('student_course', models.CharField(max_length=10)),
                ('student_class10_board', models.CharField(default='Null', max_length=20)),
                ('student_class10_perc', models.CharField(default='Null', max_length=20)),
                ('student_class10_year_of_pass', models.CharField(default='Null', max_length=20)),
                ('student_class12_board', models.CharField(default='Null', max_length=20)),
                ('student_class12_perc', models.CharField(default='Null', max_length=20)),
                ('student_class12_year_of_pass', models.CharField(default='Null', max_length=20)),
                ('student_graduation_board', models.CharField(default='Null', max_length=20)),
                ('student_graduation_perc', models.CharField(default='Null', max_length=20)),
                ('student_graduation_year_of_pass', models.CharField(default='Null', max_length=20)),
                ('student_masters_board', models.CharField(default='Null', max_length=20)),
                ('student_masters_perc', models.CharField(default='Null', max_length=20)),
                ('student_masters_year_of_pass', models.CharField(default='Null', max_length=20)),
            ],
            options={
                'verbose_name': 'Students Data',
            },
        ),
    ]