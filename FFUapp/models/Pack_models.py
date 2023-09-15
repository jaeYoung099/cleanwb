from django.db import models

class APack(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, pack_price) found, that is not supported. The first column is selected.
    pack_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'a_pack'
        unique_together = (('size', 'pack_price'),)

class BPack(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, pack_price) found, that is not supported. The first column is selected.
    pack_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'b_pack'
        unique_together = (('size', 'pack_price'),)

class CPack(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, pack_price) found, that is not supported. The first column is selected.
    pack_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'c_pack'
        unique_together = (('size', 'pack_price'),)

class DPack(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, pack_price) found, that is not supported. The first column is selected.
    pack_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'd_pack'
        unique_together = (('size', 'pack_price'),)

class EPack(models.Model):
    size = models.CharField(primary_key=True, max_length=16)  # The composite primary key (size, pack_price) found, that is not supported. The first column is selected.
    pack_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'e_pack'
        unique_together = (('size', 'pack_price'),)
