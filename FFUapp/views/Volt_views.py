from django.shortcuts import render
from FFUapp.models.Volt_models import AVolt, BVolt, CVolt, DVolt, EVolt

# Volt : spec별 grade table 선택
def calculate_volt_price(size, spec):
    try:    
        if spec == "A 등급":
            model = AVolt
        elif spec == "B 등급":
            model = BVolt
        elif spec == "C 등급":
            model = CVolt
        elif spec == "D 등급":
            model = DVolt
        elif spec == "E 등급":
            model = EVolt
        else:
            return 0

        # 입력값을 통해 Primary key로 지정하여 ORM            
        volts = model.objects.filter(size=size)

        # VOLT 가격 계산        
        volt_subtotal = 0
        for volt in volts:
            volt_amount = volt.volt_price * volt.volt_count
            volt_subtotal += volt_amount

        calculate_volt_price = volt_subtotal * 1.5
        return calculate_volt_price

    except Exception as e:
        print(f"Error occurred: {e}")
        return 0