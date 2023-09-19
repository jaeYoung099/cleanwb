from django.shortcuts import render
from FFUapp.models.Paint_models import APaint, BPaint, CPaint, DPaint, EPaint

# 도장비 : spec별 grade table 선택
def calculate_paint_price(size, spec):
    try:    
        if spec == "A 등급":
            model = APaint
        elif spec == "B 등급":
            model = BPaint
        elif spec == "C 등급":
            model = CPaint
        elif spec == "D 등급":
            model = DPaint
        elif spec == "E 등급":
            model = EPaint
        else:
            return 0

        # 입력값을 통해 Primary key로하여 데이터조회
        paints = model.objects.filter(size=size)

        # 도장비 가격 계산
        total_paint_cost = 0  
        for paint in paints:
            square_meter = ((paint.figure_width * paint.figure_length)/1000000) * 2 * paint.necessary_quantity
            paint_cost = square_meter * paint.won_per_meter    

            total_paint_cost += paint_cost  

        return total_paint_cost
        
    except Exception as e:
        print(f"Error occurred: {e}")
        return 0