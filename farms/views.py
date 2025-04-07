from rest_framework import generics
from .models import *
from .serializers import *

class AgricultureDataCreate(generics.CreateAPIView):
    queryset = AgricultureFarm.objects.all()
    serializer_class = AgricultureSerializer

class CattleDataCreate(generics.CreateAPIView):
    queryset = CattleFarm.objects.all()
    serializer_class = CattleSerializer

class PoultryDataCreate(generics.CreateAPIView):
    queryset = PoultryFarm.objects.all()
    serializer_class = PoultrySerializer

class FisheriesDataCreate(generics.CreateAPIView):
    queryset = Fisheries.objects.all()
    serializer_class = FisheriesSerializer