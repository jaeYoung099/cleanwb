from django.db import models

# 자재비 모델
class AMaterialcost(models.Model):
    item = models.CharField(primary_key=True, max_length=32)  
    size = models.CharField(max_length=16)
    matherialsize_width = models.FloatField()
    matherialsize_length = models.FloatField()
    rawmaterial_thickness = models.FloatField()
    rawmaterial_density = models.FloatField()
    manufacture_quantity = models.IntegerField()
    necessary_quantity = models.IntegerField()
    won_per_kg = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'a_materialcost'
        unique_together = (('item', 'size'),)

class BMaterialcost(models.Model):
    item = models.CharField(primary_key=True, max_length=32)  
    size = models.CharField(max_length=16)
    matherialsize_width = models.FloatField()
    matherialsize_length = models.FloatField()
    rawmaterial_thickness = models.FloatField()
    rawmaterial_density = models.FloatField()
    manufacture_quantity = models.IntegerField()
    necessary_quantity = models.IntegerField()
    won_per_kg = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'b_materialcost'
        unique_together = (('item', 'size'),)

class CMaterialcost(models.Model):
    item = models.CharField(primary_key=True, max_length=32)  
    size = models.CharField(max_length=16)
    matherialsize_width = models.FloatField()
    matherialsize_length = models.FloatField()
    rawmaterial_thickness = models.FloatField()
    rawmaterial_density = models.FloatField()
    manufacture_quantity = models.IntegerField()
    necessary_quantity = models.IntegerField()
    won_per_kg = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'c_materialcost'
        unique_together = (('item', 'size'),)

class DMaterialcost(models.Model):
    item = models.CharField(primary_key=True, max_length=32)  
    size = models.CharField(max_length=16)
    matherialsize_width = models.FloatField()
    matherialsize_length = models.FloatField()
    rawmaterial_thickness = models.FloatField()
    rawmaterial_density = models.FloatField()
    manufacture_quantity = models.IntegerField()
    necessary_quantity = models.IntegerField()
    won_per_kg = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'd_materialcost'
        unique_together = (('item', 'size'),)

class EMaterialcost(models.Model):
    item = models.CharField(primary_key=True, max_length=32)  
    size = models.CharField(max_length=16)
    matherialsize_width = models.FloatField()
    matherialsize_length = models.FloatField()
    rawmaterial_thickness = models.FloatField()
    rawmaterial_density = models.FloatField()
    manufacture_quantity = models.IntegerField()
    necessary_quantity = models.IntegerField()
    won_per_kg = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'e_materialcost'
        unique_together = (('item', 'size'),)
