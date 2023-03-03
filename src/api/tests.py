from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import WeatherData, WeatherCalculation
from .serializers import WeatherDataSerializer, WeatherCalculationSerializer


class WeatherDataListTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

        # create some sample weather data objects
        WeatherData.objects.create(station_id='USC00110187', date='1985-01-01', max_temp=200, min_temp=100, precipitation=0)
        WeatherData.objects.create(station_id='USC00110172', date='1985-01-01', max_temp=250, min_temp=150, precipitation=10)
        WeatherData.objects.create(station_id='USC00110187', date='1985-02-01', max_temp=150, min_temp=50, precipitation=5)

    def test_get_weather_data_list(self):
        response = self.client.get(reverse('weather-data-list'))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # check that all objects are returned
        queryset = WeatherData.objects.all().order_by('date', 'station_id')
        serializer = WeatherDataSerializer(queryset, many=True)
        self.assertEqual(response.data['results'], serializer.data)

    def test_filter_by_station_id(self):
        response = self.client.get(reverse('weather-data-list'), {'station_id': 'USC00110187'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # check that only objects with station_id 'USC00110187' are returned
        queryset = WeatherData.objects.filter(station_id='USC00110187').order_by('date', 'station_id')
        serializer = WeatherDataSerializer(queryset, many=True)
        self.assertEqual(response.data['results'], serializer.data)

    def test_filter_by_date(self):
        response = self.client.get(reverse('weather-data-list'), {'date': '1985-01-01'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # check that only objects with date '1985-01-01' are returned
        queryset = WeatherData.objects.filter(date='1985-01-01').order_by('date', 'station_id')
        serializer = WeatherDataSerializer(queryset, many=True)
        self.assertEqual(response.data['results'], serializer.data)

    def test_filter_by_station_id_and_date(self):
        response = self.client.get(reverse('weather-data-list'), {'station_id': 'USC00110187', 'date': '1985-01-01'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # check that only objects with station_id 'USC00110187' and date '1985-01-01' are returned
        queryset = WeatherData.objects.filter(station_id='USC00110187', date='1985-01-01').order_by('date', 'station_id')
        serializer = WeatherDataSerializer(queryset, many=True)
        self.assertEqual(response.data['results'], serializer.data)


class WeatherCalculationListTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse('weather-calculation-list')

        # create some sample weather calculation objects
        self.calculation_1 = WeatherCalculation.objects.create(
            station_id=1, year=2020, avg_max_temp=80.0, avg_min_temp=40.0, total_precipitation=60.0
        )
        self.calculation_2 = WeatherCalculation.objects.create(
            station_id=2, year=2021, avg_max_temp=85.0, avg_min_temp=45.0, total_precipitation=65.0
        )

    def test_get_weather_calculations(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Check that the API returns a list of weather calculations
        expected_data = WeatherCalculationSerializer([self.calculation_1, self.calculation_2], many=True).data
        self.assertEqual(response.data['results'], expected_data)

    def test_filter_weather_calculations_by_station_id(self):
        response = self.client.get(self.url, {'station_id': 1})
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # check that only objects with station_id '1' are returned
        expected_data = WeatherCalculationSerializer([self.calculation_1], many=True).data
        self.assertEqual(response.data['results'], expected_data)




