from django.shortcuts import render
from FFUapp.models.Jab_models import AJab, BJab, CJab, DJab, EJab

# 포장용잡자재 : spec별 grade table 선택
def calculate_jab_price(size, spec):
    try:    
        if spec == "A 등급":
            model = AJab
        elif spec == "B 등급":
            model = BJab
        elif spec == "C 등급":
            model = CJab
        elif spec == "D 등급":
            model = DJab
        elif spec == "E 등급":
            model = EJab
        else:
            return 0 

        # 입력값을 통해 Primary key로 지정하여 ORM
        jab = model.objects.filter(size=size).first()
        if jab:
            return jab.jab_price
        else:
            return 0  
            
    except Exception as e:
        print(f"Error occurred: {e}")
        return 0