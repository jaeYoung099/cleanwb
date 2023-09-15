from django.db import models

class AVolt(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, volt_name) found, that is not supported. The first column is selected.
    volt_name = models.CharField(max_length=50)
    volt_price = models.FloatField()
    volt_count = models.FloatField()

    class Meta:
        managed = False
        db_table = 'a_volt'
        unique_together = (('size', 'volt_name'),)

class BVolt(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, volt_name) found, that is not supported. The first column is selected.
    volt_name = models.CharField(max_length=50)
    volt_price = models.FloatField()
    volt_count = models.FloatField()

    class Meta:
        managed = False
        db_table = 'b_volt'
        unique_together = (('size', 'volt_name'),)

class CVolt(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, volt_name) found, that is not supported. The first column is selected.
    volt_name = models.CharField(max_length=50)
    volt_price = models.FloatField()
    volt_count = models.FloatField()

    class Meta:
        managed = False
        db_table = 'c_volt'
        unique_together = (('size', 'volt_name'),)

class DVolt(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, volt_name) found, that is not supported. The first column is selected.
    volt_name = models.CharField(max_length=50)
    volt_price = models.FloatField()
    volt_count = models.FloatField()

    class Meta:
        managed = False
        db_table = 'd_volt'
        unique_together = (('size', 'volt_name'),)

class EVolt(models.Model):
    size = models.CharField(primary_key=True, max_length=50)  # The composite primary key (size, volt_name) found, that is not supported. The first column is selected.
    volt_name = models.CharField(max_length=50)
    volt_price = models.FloatField()
    volt_count = models.FloatField()

    class Meta:
        managed = False
        db_table = 'e_volt'
        unique_together = (('size', 'volt_name'),)
