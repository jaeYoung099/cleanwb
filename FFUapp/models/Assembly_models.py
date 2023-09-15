from django.db import models

class AAssembly(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, assembly_price) found, that is not supported. The first column is selected.
    assembly_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'a_assembly'
        unique_together = (('size', 'assembly_price'),)

class BAssembly(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, assembly_price) found, that is not supported. The first column is selected.
    assembly_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'b_assembly'
        unique_together = (('size', 'assembly_price'),)

class CAssembly(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, assembly_price) found, that is not supported. The first column is selected.
    assembly_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'c_assembly'
        unique_together = (('size', 'assembly_price'),)

class DAssembly(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, assembly_price) found, that is not supported. The first column is selected.
    assembly_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'd_assembly'
        unique_together = (('size', 'assembly_price'),)

class EAssembly(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, assembly_price) found, that is not supported. The first column is selected.
    assembly_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'e_assembly'
        unique_together = (('size', 'assembly_price'),)

