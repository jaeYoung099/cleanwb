from django.shortcuts import render
from FFUapp.models.NCT_models import ANct, BNct, CNct, DNct, ENct

# NCT : spec별 grade table 선택
def calculate_nct_price(size, spec):
    try:    
        if spec == "A 등급":
            model = ANct
        elif spec == "B 등급":
            model = BNct
        elif spec == "C 등급":
            model = CNct
        elif spec == "D 등급":
            model = DNct
        elif spec == "E 등급":
            model = ENct
        else:
            return 0
            
        # 입력값을 통해 Primary key로 지정하여 ORM
        nct = model.objects.filter(size=size).first()
        if nct:
            return nct.nct_price
        else:
            return 0

    except Exception as e:
        print(f"Error occurred: {e}")
        return 0
