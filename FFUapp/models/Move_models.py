from django.db import models

# 운반비 모델 (차량대수)
class LoadQuantity(models.Model):
    size = models.CharField(primary_key=True, max_length=50)
    ea = models.IntegerField()
    carsize = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'load_quantity'
        unique_together = (('size', 'ea'),)

# 운반비 모델 (운송위치)
class LocationMovecost(models.Model):
    location = models.CharField(primary_key=True, max_length=50)  
    carsize = models.CharField(max_length=50)
    move_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'location_movecost'
        unique_together = (('location', 'carsize'),)