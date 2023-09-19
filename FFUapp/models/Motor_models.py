from django.db import models

# MOTOR 모델
class AMotor(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    motortype = models.CharField(max_length=16)
    ph = models.CharField(max_length=32)
    motor_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'a_motor'
        unique_together = (('size', 'motortype', 'ph'),)

class BMotor(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    motortype = models.CharField(max_length=16)
    ph = models.CharField(max_length=32)
    motor_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'b_motor'
        unique_together = (('size', 'motortype', 'ph'),)

class CMotor(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    motortype = models.CharField(max_length=16)
    ph = models.CharField(max_length=32)
    motor_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'c_motor'
        unique_together = (('size', 'motortype', 'ph'),)

class DMotor(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    motortype = models.CharField(max_length=16)
    ph = models.CharField(max_length=32)
    motor_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'd_motor'
        unique_together = (('size', 'motortype', 'ph'),)

class EMotor(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    motortype = models.CharField(max_length=16)
    ph = models.CharField(max_length=32)
    motor_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'e_motor'
        unique_together = (('size', 'motortype', 'ph'),)
