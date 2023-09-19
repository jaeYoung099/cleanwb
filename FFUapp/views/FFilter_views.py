from django.shortcuts import render
from FFUapp.models.FFilter_models import AFilter, BFilter, CFilter, DFilter, EFilter

# FILTER : spec별 grade table 선택
def calculate_ffilter_price(size, spec, filterstyle):
    try:    
        if spec == "A 등급":
            model = AFilter
        elif spec == "B 등급":
            model = BFilter
        elif spec == "C 등급":
            model = CFilter
        elif spec == "D 등급":
            model = DFilter
        elif spec == "E 등급":
            model = EFilter
        else:
            return 0

        # 입력값을 통해 Primary key로 지정하여 ORM
        ffilter = model.objects.filter(
            size=size,
            filterstyle=filterstyle 
        ).first() 

        if ffilter:
            return ffilter.filter_price 
        else:
            return 0

    except Exception as e:
        print(f"Error occurred: {e}")
        return 0

        