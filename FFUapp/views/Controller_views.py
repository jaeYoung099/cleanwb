from django.shortcuts import render
from FFUapp.models.Controller_models import AController, BController, CController, DController, EController

# 컨트롤러 : spec별 grade table 선택
def calculate_controller_price(size, spec, motortype, ph):
    try:    
        if spec == "A 등급":
            model = AController
        elif spec == "B 등급":
            model = BController
        elif spec == "C 등급":
            model = CController
        elif spec == "D 등급":
            model = DController
        elif spec == "E 등급":
            model = EController
        else:
            return 0

        controller = model.objects.filter(
            size=size,
            motortype=motortype, 
            ph=ph
        ).first() 

        # 입력값을 통해 Primary key로 지정하여 ORM
        if controller:
            return controller.controller_price 
        else:
            return 0 

    except Exception as e:
        print(f"Error occurred: {e}")  
        return 0

        