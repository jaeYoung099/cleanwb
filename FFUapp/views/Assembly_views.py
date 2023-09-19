from django.shortcuts import render
from FFUapp.models.Assembly_models import AAssembly, BAssembly, CAssembly, DAssembly, EAssembly

# 조립인건비 : spec별 grade table 선택
def calculate_assembly_price(size, spec):
    try:    
        if spec == "A 등급":
            model = AAssembly
        elif spec == "B 등급":
            model = BAssembly
        elif spec == "C 등급":
            model = CAssembly
        elif spec == "D 등급":
            model = DAssembly
        elif spec == "E 등급":
            model = EAssembly                           
        else:
            return 0
            
        # 입력값을 통해 Primary key로 지정하여 ORM
        assembly = model.objects.filter(size=size).first()
        if assembly:
            return assembly.assembly_price 
        else:
            return 0  
        
    except Exception as e:
        print(f"Error occurred: {e}")
        return 0