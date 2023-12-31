from django.db import models

# 컨트롤러 모델
class AController(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    motortype = models.CharField(max_length=16)
    ph = models.CharField(max_length=32)
    controller_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'a_controller'
        unique_together = (('size', 'motortype', 'ph'),)

class BController(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    motortype = models.CharField(max_length=16)
    ph = models.CharField(max_length=32)
    controller_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'b_controller'
        unique_together = (('size', 'motortype', 'ph'),)

class CController(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    motortype = models.CharField(max_length=16)
    ph = models.CharField(max_length=32)
    controller_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'c_controller'
        unique_together = (('size', 'motortype', 'ph'),)

class DController(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    motortype = models.CharField(max_length=16)
    ph = models.CharField(max_length=32)
    controller_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'd_controller'
        unique_together = (('size', 'motortype', 'ph'),)

class EController(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    motortype = models.CharField(max_length=16)
    ph = models.CharField(max_length=32)
    controller_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'e_controller'
        unique_together = (('size', 'motortype', 'ph'),)
