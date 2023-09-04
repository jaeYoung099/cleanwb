from django.urls import path
from FFUapp.views import testmove_views  # views를 임포트해야 합니다
from FFUapp.views import command_views  # FFUapp/views 폴더 내의 views.py 가져오기

urlpatterns = [
    path('FFUInput/', command_views.ffuInput),
    path('FFUOutput/', command_views.ffuOutput),
    path('FFUDashboard/', command_views.ffuDashboard),
    path('download_excel/', command_views.download_excel, name='download_excel'),
    path('test/', command_views.test, name='test'),
    path('test/<str:selected_size>/', testmove_views.test_function, name='test_with_size'),  # URL 패턴 수정
]
