from django.db import models

# 도장비 모델
class APaint(models.Model):
    item = models.CharField(primary_key=True, max_length=32)
    size = models.CharField(max_length=16)
    figure_width = models.FloatField()
    figure_length = models.FloatField()
    won_per_meter = models.IntegerField()
    necessary_quantity = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'a_paint'
        unique_together = (('item', 'size'),)

class BPaint(models.Model):
    item = models.CharField(primary_key=True, max_length=32)
    size = models.CharField(max_length=16)
    figure_width = models.FloatField()
    figure_length = models.FloatField()
    won_per_meter = models.IntegerField()
    necessary_quantity = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'b_paint'
        unique_together = (('item', 'size'),)

class CPaint(models.Model):
    item = models.CharField(primary_key=True, max_length=32)
    size = models.CharField(max_length=16)
    figure_width = models.FloatField()
    figure_length = models.FloatField()
    won_per_meter = models.IntegerField()
    necessary_quantity = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'c_paint'
        unique_together = (('item', 'size'),)

class DPaint(models.Model):
    item = models.CharField(primary_key=True, max_length=32)
    size = models.CharField(max_length=16)
    figure_width = models.FloatField()
    figure_length = models.FloatField()
    won_per_meter = models.IntegerField()
    necessary_quantity = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'd_paint'
        unique_together = (('item', 'size'),)

class EPaint(models.Model):
    item = models.CharField(primary_key=True, max_length=32)
    size = models.CharField(max_length=16)
    figure_width = models.FloatField()
    figure_length = models.FloatField()
    won_per_meter = models.IntegerField()
    necessary_quantity = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'e_paint'
        unique_together = (('item', 'size'),)
