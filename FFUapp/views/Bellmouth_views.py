from django.shortcuts import render
from FFUapp.models.Bellmouth_models import ABellmouth, BBellmouth, CBellmouth, DBellmouth, EBellmouth

# 벨마우스 : spec별 grade table 선택
def calculate_bellmouth_price(size, spec, motortype):
    try:    
        if spec == "A 등급":
            model = ABellmouth
        elif spec == "B 등급":
            model = BBellmouth
        elif spec == "C 등급":
            model = CBellmouth
        elif spec == "D 등급":
            model = DBellmouth
        elif spec == "E 등급":
            model = EBellmouth            
        else:
            return 0

        bellmouth = model.objects.filter(
            size=size,
            motortype=motortype
        ).first() 

        # 입력값을 통해 Primary key로 지정하여 ORM
        if bellmouth:
            return bellmouth.bellmouth_price 
        else:
            return 0 

    except Exception as e:
        print(f"Error occurred: {e}")  
        return 0

        