from django.shortcuts import render
from FFUapp.models.MaterialCost_models import AMaterialcost, BMaterialcost, CMaterialcost, DMaterialcost, EMaterialcost

# 자재비 : spec별 grade table 선택
def calculate_materialcost_price(size, spec):
    try:    
        if spec == "A 등급":
            model = AMaterialcost
        elif spec == "B 등급":
            model = BMaterialcost
        elif spec == "C 등급":
            model = CMaterialcost
        elif spec == "D 등급":
            model = DMaterialcost
        elif spec == "E 등급":
            model = EMaterialcost
        else:
            return 0  

        # 입력값을 통해 Primary key로 지정하여 ORM
        materialcosts = model.objects.filter(size=size)
        
        if not materialcosts.exists():
            return 0

        # 자재비 가격 계산
        calculate_materialcost_price = 0
        for materialcost in materialcosts:
            if materialcost.manufacture_quantity == 0:
                materialcost_weight = 0
            else:
                materialcost_weight = (materialcost.matherialsize_width * materialcost.matherialsize_length * materialcost.rawmaterial_thickness * materialcost.rawmaterial_density / (1000000 * materialcost.manufacture_quantity)) * materialcost.necessary_quantity
        
            rawmaterial_cost = materialcost_weight * materialcost.won_per_kg
            calculate_materialcost_price += rawmaterial_cost

        return calculate_materialcost_price

    except Exception as e:
        print(f"Error occurred: {e}")
        return 0

