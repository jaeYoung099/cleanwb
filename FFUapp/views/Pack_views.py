from django.shortcuts import render
from FFUapp.models.Pack_models import APack, BPack, CPack, DPack, EPack

# 포장용팔렛트 : spec별 grade table 선택
def calculate_pack_price(size, spec):
    try:    
        if spec == "A 등급":
            model = APack
        elif spec == "B 등급":
            model = BPack
        elif spec == "C 등급":
            model = CPack
        elif spec == "D 등급":
            model = DPack
        elif spec == "E 등급":
            model = EPack
        else:
            return 0

        # 입력값을 통해 Primary key로 지정하여 ORM
        pack = model.objects.filter(size=size).first()
        if pack:
            return pack.pack_price 
        else:
            return 0
              
    except Exception as e:
        print(f"Error occurred: {e}")
        return 0