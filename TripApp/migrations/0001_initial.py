# Generated by Django 4.0.4 on 2022-08-26 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trip_Master_TripSettingDetails',
            fields=[
                ('trip_setting_details_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('repeat_on', models.IntegerField(default=False)),
                ('repeat_start_date', models.DateField(null=True)),
                ('repeat_end_date', models.DateField(blank=True)),
                ('trip_start_time', models.TimeField(blank=True)),
                ('pricing_per_km', models.IntegerField(default=0)),
                ('is_deleted', models.CharField(max_length=20)),
            ],
            options={
                'db_table': 'TripSettingDetails',
            },
        ),
        migrations.CreateModel(
            name='Trip_Master_TripDetails',
            fields=[
                ('trip_id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('fleet_id', models.CharField(max_length=100)),
                ('vehicle_id', models.CharField(max_length=100)),
                ('driver_id', models.CharField(max_length=100)),
                ('start_date_time', models.DateField(null=True)),
                ('end_date_time', models.DateField(null=True)),
                ('trip_status', models.CharField(max_length=100)),
                ('is_cancel', models.CharField(max_length=20)),
                ('is_deleted', models.CharField(max_length=20)),
                ('trip_settings_fk', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TripApp.trip_master_tripsettingdetails')),
            ],
            options={
                'db_table': 'TripDetails',
            },
        ),
    ]
