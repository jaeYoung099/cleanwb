from django.db import models

# Filter 모델
class AFilter(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    filterstyle = models.CharField(max_length=16)
    filter_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'a_filter'
        unique_together = (('size', 'filterstyle'),)

class BFilter(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    filterstyle = models.CharField(max_length=16)
    filter_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'b_filter'
        unique_together = (('size', 'filterstyle'),)

class CFilter(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    filterstyle = models.CharField(max_length=16)
    filter_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'c_filter'
        unique_together = (('size', 'filterstyle'),)


class DFilter(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    filterstyle = models.CharField(max_length=16)
    filter_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'd_filter'
        unique_together = (('size', 'filterstyle'),)

class EFilter(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    filterstyle = models.CharField(max_length=16)
    filter_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'e_filter'
        unique_together = (('size', 'filterstyle'),)
