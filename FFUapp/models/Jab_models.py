from django.db import models

class AJab(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    jab_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'a_jab'

class BJab(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    jab_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'b_jab'

class CJab(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    jab_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'c_jab'

class DJab(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    jab_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'd_jab'

class EJab(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    jab_price = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'e_jab'
