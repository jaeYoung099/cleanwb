from django.shortcuts import render
from FFUapp.models.Jab_models import AJab, BJab, CJab, DJab, EJab

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

        jab = model.objects.filter(size=size).first()
        if jab:
            return jab.jab_price
        else:
            return 0  
            
    except Exception as e:
        print(f"Error occurred: {e}")
        return 0