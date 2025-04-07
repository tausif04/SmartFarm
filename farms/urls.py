from django.urls import path
from .views import *

urlpatterns = [
    path('agriculture/', AgricultureDataCreate.as_view(), name='agriculture-data'),
    path('cattle/', CattleDataCreate.as_view(), name='cattle-data'),
    path('poultry/', PoultryDataCreate.as_view(), name='poultry-data'),
    path('fisheries/', FisheriesDataCreate.as_view(), name='fisheries-data'),
]