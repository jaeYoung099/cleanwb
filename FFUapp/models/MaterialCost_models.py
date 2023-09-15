from django.db import models

class AMaterialcost(models.Model):
    item = models.CharField(primary_key=True, max_length=32)  # The composite primary key (item, size) found, that is not supported. The first column is selected.
    size = models.CharField(max_length=16)
    matherialsize_width = models.FloatField()
    matherialsize_length = models.FloatField()
    rawmaterial_thickness = models.FloatField()
    rawmaterial_density = models.FloatField()
    manufacture_quantity = models.IntegerField()
    necessary_quantity = models.IntegerField()
    won_per_kg = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'a_materialcost'
        unique_together = (('item', 'size'),)

class BMaterialcost(models.Model):
    item = models.CharField(primary_key=True, max_length=32)  # The composite primary key (item, size) found, that is not supported. The first column is selected.
    size = models.CharField(max_length=16)
    matherialsize_width = models.FloatField()
    matherialsize_length = models.FloatField()
    rawmaterial_thickness = models.FloatField()
    rawmaterial_density = models.FloatField()
    manufacture_quantity = models.IntegerField()
    necessary_quantity = models.IntegerField()
    won_per_kg = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'b_materialcost'
        unique_together = (('item', 'size'),)

class CMaterialcost(models.Model):
    item = models.CharField(primary_key=True, max_length=32)  # The composite primary key (item, size) found, that is not supported. The first column is selected.
    size = models.CharField(max_length=16)
    matherialsize_width = models.FloatField()
    matherialsize_length = models.FloatField()
    rawmaterial_thickness = models.FloatField()
    rawmaterial_density = models.FloatField()
    manufacture_quantity = models.IntegerField()
    necessary_quantity = models.IntegerField()
    won_per_kg = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'c_materialcost'
        unique_together = (('item', 'size'),)

class DMaterialcost(models.Model):
    item = models.CharField(primary_key=True, max_length=32)  # The composite primary key (item, size) found, that is not supported. The first column is selected.
    size = models.CharField(max_length=16)
    matherialsize_width = models.FloatField()
    matherialsize_length = models.FloatField()
    rawmaterial_thickness = models.FloatField()
    rawmaterial_density = models.FloatField()
    manufacture_quantity = models.IntegerField()
    necessary_quantity = models.IntegerField()
    won_per_kg = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'd_materialcost'
        unique_together = (('item', 'size'),)

class EMaterialcost(models.Model):
    item = models.CharField(primary_key=True, max_length=32)  # The composite primary key (item, size) found, that is not supported. The first column is selected.
    size = models.CharField(max_length=16)
    matherialsize_width = models.FloatField()
    matherialsize_length = models.FloatField()
    rawmaterial_thickness = models.FloatField()
    rawmaterial_density = models.FloatField()
    manufacture_quantity = models.IntegerField()
    necessary_quantity = models.IntegerField()
    won_per_kg = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'e_materialcost'
        unique_together = (('item', 'size'),)
