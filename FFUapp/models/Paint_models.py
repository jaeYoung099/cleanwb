from django.db import models

class APaint(models.Model):
    item = models.CharField(primary_key=True, max_length=32)  # The composite primary key (item, size) found, that is not supported. The first column is selected.
    size = models.CharField(max_length=16)
    figure_width = models.FloatField()
    figure_length = models.FloatField()
    won_per_meter = models.IntegerField()
    necessary_quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'a_paint'
        unique_together = (('item', 'size'),)

class BPaint(models.Model):
    item = models.CharField(primary_key=True, max_length=32)  # The composite primary key (item, size) found, that is not supported. The first column is selected.
    size = models.CharField(max_length=16)
    figure_width = models.FloatField()
    figure_length = models.FloatField()
    won_per_meter = models.IntegerField()
    necessary_quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'b_paint'
        unique_together = (('item', 'size'),)

class CPaint(models.Model):
    item = models.CharField(primary_key=True, max_length=32)  # The composite primary key (item, size) found, that is not supported. The first column is selected.
    size = models.CharField(max_length=16)
    figure_width = models.FloatField()
    figure_length = models.FloatField()
    won_per_meter = models.IntegerField()
    necessary_quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'c_paint'
        unique_together = (('item', 'size'),)

class DPaint(models.Model):
    item = models.CharField(primary_key=True, max_length=32)  # The composite primary key (item, size) found, that is not supported. The first column is selected.
    size = models.CharField(max_length=16)
    figure_width = models.FloatField()
    figure_length = models.FloatField()
    won_per_meter = models.IntegerField()
    necessary_quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'd_paint'
        unique_together = (('item', 'size'),)

class EPaint(models.Model):
    item = models.CharField(primary_key=True, max_length=32)  # The composite primary key (item, size) found, that is not supported. The first column is selected.
    size = models.CharField(max_length=16)
    figure_width = models.FloatField()
    figure_length = models.FloatField()
    won_per_meter = models.IntegerField()
    necessary_quantity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'e_paint'
        unique_together = (('item', 'size'),)
