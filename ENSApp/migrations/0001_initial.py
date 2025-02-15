# Generated by Django 3.1.8 on 2023-07-05 11:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Total_Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_type', models.CharField(max_length=10)),
                ('date', models.DateField(auto_now_add=True)),
                ('punchin_from', models.CharField(max_length=200)),
                ('punchin_to', models.CharField(max_length=200)),
                ('punchout_from', models.CharField(max_length=200)),
                ('punchout_to', models.CharField(max_length=200)),
                ('morning_reading', models.IntegerField(default=0, verbose_name='Manual Reading')),
                ('evening_reading', models.IntegerField(default=0, verbose_name='Manual Reading')),
                ('ticket', models.IntegerField(default=0)),
                ('d_a', models.IntegerField(default=0, verbose_name='DA')),
                ('lodging_boarding', models.IntegerField(default=0, verbose_name='Lodging/Boarding')),
                ('daily_km', models.IntegerField(default=0)),
                ('daily_cost', models.FloatField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Total Expense',
            },
        ),
        migrations.CreateModel(
            name='Punch_Out',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('time', models.TimeField(auto_now_add=True, null=True)),
                ('from_location', models.CharField(max_length=100)),
                ('to_location', models.CharField(max_length=100)),
                ('meter_photo', models.ImageField(upload_to='meter_photos/', verbose_name='Meter Photo')),
                ('manual_reading', models.IntegerField(default=0, verbose_name='Manual Reading')),
                ('ticket_amount', models.IntegerField(default=0)),
                ('ticket_photo', models.ImageField(null=True, upload_to='meter_photos/')),
                ('daily_allounce', models.IntegerField(default=0, verbose_name='DA')),
                ('lodging', models.IntegerField(default=0, verbose_name='Lodging/Boarding')),
                ('lodging_photo', models.ImageField(blank=True, null=True, upload_to='meter_photos/')),
                ('todays_work', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Punch Out',
            },
        ),
        migrations.CreateModel(
            name='Punch_In',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now_add=True, null=True)),
                ('time', models.TimeField(auto_now_add=True, null=True)),
                ('vehicle_type', models.CharField(choices=[('2 wheeler', 'Two Wheeler'), ('4 wheeler', 'Four Wheeler'), ('By Train', 'By Train'), ('By Bus', 'By Bus'), ('By Auto', 'By Auto')], max_length=9)),
                ('from_location', models.CharField(default='Home', max_length=100)),
                ('to_location', models.CharField(default='Office', max_length=100)),
                ('meter_photo', models.ImageField(null=True, upload_to='meter_photos/', verbose_name='Meter Photo')),
                ('manual_reading', models.IntegerField(default=0, verbose_name='Manual Reading')),
                ('ticket_amount', models.IntegerField(default=0)),
                ('ticket_photo', models.ImageField(null=True, upload_to='meter_photos/')),
                ('todays_work', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Punch In',
            },
        ),
        migrations.CreateModel(
            name='EmployeeProfile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_picture', models.ImageField(default='default.png', upload_to='images/')),
                ('department', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('vehicle_number', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=20)),
                ('birth_date', models.DateField(blank=True, null=True)),
                ('address', models.CharField(max_length=200)),
                ('work_location', models.CharField(blank=True, max_length=30)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Daily_Attendance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intime', models.TimeField(null=True)),
                ('outtime', models.TimeField(null=True)),
                ('date', models.DateField(auto_now_add=True)),
                ('present', models.CharField(max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Daily Attendance',
            },
        ),
    ]
