from django.db import models

class Category(models.Model):
    category_id=models.IntegerField(primary_key=True)
    category_name=models.CharField(max_length=100)
    created_by=models.CharField(max_length=50,default="1")
    modified_by=models.CharField(max_length=50,default="1")
    is_deleted=models.BooleanField(default=False)
    modified_date_time=models.DateTimeField(blank=True,null=True)
    created_date_time=models.DateTimeField(blank=True,null=True)

    class Meta:
        db_table="Category"

class BusDetails(models.Model):
    vin=models.IntegerField(primary_key=True)
    vehicle_id=models.CharField(max_length=100)
    model_number=models.CharField(max_length=100)
    model=models.CharField(max_length=100)
    fuel_type=models.CharField(max_length=100)
    number_seats=models.IntegerField()
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    created_by=models.CharField(max_length=50,default="1")
    modified_by=models.CharField(max_length=50,default="1")
    is_deleted=models.BooleanField(default=False)
    modified_date_time=models.DateTimeField(blank=True,null=True)
    created_date_time=models.DateTimeField(blank=True,null=True)

    class Meta:
        db_table="BusDetails"