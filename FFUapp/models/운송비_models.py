from django.db import Fan_models

# 장비size별 차량 적재 수량
class LoadQuantity(models.Model):
    size = models.CharField(primary_key=True, max_length=50)            # FFU 규격
    ffucount = models.IntegerField()                                    # FFU 갯수 EA
    carsize = models.IntegerField()                                     # 차량 ton 수

    class Meta:
        managed = False
        db_table = 'load_quantity'
        unique_together = (('size', 'ffucount'),)


class LocationMovecost(models.Model):
    location = models.CharField(primary_key=True, max_length=50)
    number_1ton = models.IntegerField(db_column='1ton')  # Field renamed because it wasn't a valid Python identifier.
    number_5ton = models.IntegerField(db_column='5ton')  # Field renamed because it wasn't a valid Python identifier.
    number_11ton = models.IntegerField(db_column='11ton')  # Field renamed because it wasn't a valid Python identifier.

    class Meta:
        managed = False
        db_table = 'location_movecost'