from django.db import models

# Fan 모델
class AFan(models.Model):
    size = models.CharField(primary_key=True, max_length=50)
    motortype = models.CharField(max_length=50)
    fan_size = models.CharField(max_length=16)
    fan_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'a_fan'
        unique_together = (('size', 'motortype'),)

class BFan(models.Model):
    size = models.CharField(primary_key=True, max_length=50)
    motortype = models.CharField(max_length=50)
    fan_size = models.CharField(max_length=16)
    fan_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'b_fan'
        unique_together = (('size', 'motortype'),)

class CFan(models.Model):
    size = models.CharField(primary_key=True, max_length=50)
    motortype = models.CharField(max_length=50)
    fan_size = models.CharField(max_length=16)
    fan_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'c_fan'
        unique_together = (('size', 'motortype'),)

class DFan(models.Model):
    size = models.CharField(primary_key=True, max_length=50)
    motortype = models.CharField(max_length=50)
    fan_size = models.CharField(max_length=16)
    fan_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'd_fan'
        unique_together = (('size', 'motortype'),)

class EFan(models.Model):
    size = models.CharField(primary_key=True, max_length=50)
    motortype = models.CharField(max_length=50)
    fan_size = models.CharField(max_length=16)
    fan_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'e_fan'
        unique_together = (('size', 'motortype'),)
