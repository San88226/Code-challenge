from rest_framework import serializers
from api.models import WeatherCalculation, WeatherData


class WeatherDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherData
        fields = '__all__'


class WeatherCalculationSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherCalculation
        fields = '__all__'