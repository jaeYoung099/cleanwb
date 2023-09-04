from django.shortcuts import render
from FFUapp.models.Move_models import LoadQuantity
from collections import defaultdict

def get_carsize_ea_by_size(size):
    carsize_ea = defaultdict(int)
    load_data_qs = LoadQuantity.objects.filter(size=size)
    
    for item in load_data_qs:
        carsize_ea[item.carsize] = item.ea
    
    return carsize_ea

def test_function(request, selected_size):
    carsize_ea = get_carsize_ea_by_size(selected_size)
    
    return render(request, 'test.html', {'selected_size': selected_size, 'carsize_ea': carsize_ea})

