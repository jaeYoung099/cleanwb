from django.db import models

# NCT 모델
class ANct(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    nct_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'a_nct'

class BNct(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    nct_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'b_nct'

class CNct(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    nct_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'c_nct'

class DNct(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    nct_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'd_nct'

class ENct(models.Model):
    size = models.CharField(primary_key=True, max_length=16)
    nct_price = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'e_nct'
