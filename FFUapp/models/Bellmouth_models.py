from django.db import models

class ABellmouth(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, motortype) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=16)
    bellmouth_size = models.CharField(max_length=16)
    bellmouth_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'a_bellmouth'
        unique_together = (('size', 'motortype'),)

class BBellmouth(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, motortype) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=16)
    bellmouth_size = models.CharField(max_length=16)
    bellmouth_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'b_bellmouth'
        unique_together = (('size', 'motortype'),)

class CBellmouth(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, motortype) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=16)
    bellmouth_size = models.CharField(max_length=16)
    bellmouth_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'c_bellmouth'
        unique_together = (('size', 'motortype'),)

class DBellmouth(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, motortype) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=16)
    bellmouth_size = models.CharField(max_length=16)
    bellmouth_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'd_bellmouth'
        unique_together = (('size', 'motortype'),)

class EBellmouth(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, motortype) found, that is not supported. The first column is selected.
    motortype = models.CharField(max_length=16)
    bellmouth_size = models.CharField(max_length=16)
    bellmouth_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'e_bellmouth'
        unique_together = (('size', 'motortype'),)
