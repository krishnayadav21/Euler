from django.db import models

# Create your models here.
class Trip_Master_TripSettingDetails(models.Model):

    trip_setting_details_id=models.CharField(max_length=100,primary_key=True)
    repeat_on = models.IntegerField(default=False)
    repeat_start_date = models.DateField(null=True)
    repeat_end_date = models.DateField(blank=True)
    trip_start_time = models.TimeField(blank=True)
    pricing_per_km=models.IntegerField(default=0)
    is_deleted = models.CharField(max_length=20)

    class Meta:
        db_table="TripSettingDetails"

class Trip_Master_TripDetails(models.Model):
    trip_id=models.CharField(max_length=100,primary_key=True)
    fleet_id=models.CharField(max_length=100)
    vehicle_id=models.CharField(max_length=100)
    driver_id=models.CharField(max_length=100)
    trip_settings_fk=models.ForeignKey(Trip_Master_TripSettingDetails,on_delete=models.CASCADE)
    start_date_time=models.DateField(null=True)
    end_date_time=models.DateField(null=True)
    trip_status=models.CharField(max_length=100)
    is_cancel=models.CharField(max_length=20)
    is_deleted = models.CharField(max_length=20)

    class Meta:
        db_table="TripDetails"