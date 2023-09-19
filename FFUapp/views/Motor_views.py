from django.shortcuts import render
from FFUapp.models.Motor_models import AMotor, BMotor, CMotor, DMotor, EMotor

# MOTOR : spec별 grade table 선택
def calculate_motor_price(size, spec, motortype, ph):
    try:    
        if spec == "A 등급":
            model = AMotor
        elif spec == "B 등급":
            model = BMotor
        elif spec == "C 등급":
            model = CMotor
        elif spec == "D 등급":
            model = DMotor
        elif spec == "E 등급":
            model = EMotor
        else:
            return 0

        # 입력값을 통해 Primary key로 지정하여 ORM
        motor = model.objects.filter(
            size=size,
            motortype=motortype, 
            ph=ph
        ).first() 

        if motor:
            return motor.motor_price 
        else:
            return 0

    except Exception as e:
        print(f"Error occurred: {e}")  
        return 0

        