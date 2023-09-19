from django.db import models

# 벨마우스 모델
class ABellmouth(models.Model):
    size = models.CharField(primary_key=True, max_length=50)
    motortype = models.CharField(max_length=16)
    bellmouth_size = models.CharField(max_length=16)
    bellmouth_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'a_bellmouth'
        unique_together = (('size', 'motortype'),)

class BBellmouth(models.Model):
    size = models.CharField(primary_key=True, max_length=50)
    motortype = models.CharField(max_length=16)
    bellmouth_size = models.CharField(max_length=16)
    bellmouth_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'b_bellmouth'
        unique_together = (('size', 'motortype'),)

class CBellmouth(models.Model):
    size = models.CharField(primary_key=True, max_length=50)
    motortype = models.CharField(max_length=16)
    bellmouth_size = models.CharField(max_length=16)
    bellmouth_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'c_bellmouth'
        unique_together = (('size', 'motortype'),)

class DBellmouth(models.Model):
    size = models.CharField(primary_key=True, max_length=50)
    motortype = models.CharField(max_length=16)
    bellmouth_size = models.CharField(max_length=16)
    bellmouth_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'd_bellmouth'
        unique_together = (('size', 'motortype'),)

class EBellmouth(models.Model):
    size = models.CharField(primary_key=True, max_length=50)
    motortype = models.CharField(max_length=16)
    bellmouth_size = models.CharField(max_length=16)
    bellmouth_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'e_bellmouth'
        unique_together = (('size', 'motortype'),)
