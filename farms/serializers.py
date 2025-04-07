from rest_framework import serializers
from .models import *

class AgricultureSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgricultureFarm
        fields = '__all__'

class CattleSerializer(serializers.ModelSerializer):
    class Meta:
        model = CattleFarm
        fields = '__all__'

class PoultrySerializer(serializers.ModelSerializer):
    class Meta:
        model = PoultryFarm
        fields = '__all__'

class FisheriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fisheries
        fields = '__all__'