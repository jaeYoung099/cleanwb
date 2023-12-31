from django.shortcuts import render
from FFUapp.models.Fan_models import AFan, BFan, CFan, DFan, EFan

# FAN : spec별 grade table 선택
def calculate_fan_price(size, spec, motortype):
    try:    
        if spec == "A 등급":
            model = AFan
        elif spec == "B 등급":
            model = BFan
        elif spec == "C 등급":
            model = CFan
        elif spec == "D 등급":
            model = DFan
        elif spec == "E 등급":
            model = EFan
        else:
            return 0

        # 입력값을 통해 Primary key로 지정하여 ORM
        fan = model.objects.filter(
            size=size,
            motortype=motortype
        ).first() 

        if fan:
            return fan.fan_price 
        else:
            return 0 

    except Exception as e:
        print(f"Error occurred: {e}")  
        return 0

        