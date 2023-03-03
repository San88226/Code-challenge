from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, filters
from rest_framework.pagination import PageNumberPagination
from .models import WeatherData, WeatherCalculation
from .serializers import WeatherDataSerializer, WeatherCalculationSerializer


class StandardResultsSetPagination(PageNumberPagination):
    page_size = 100
    page_size_query_param = 'page_size'
    max_page_size = 1000


def filter_queryset(queryset, request):
    station_id = request.query_params.get('station_id')
    date = request.query_params.get('date')

    if station_id:
        queryset = queryset.filter(station_id=station_id)

    if date:
        queryset = queryset.filter(date=date)

    return queryset


class WeatherDataList(generics.ListAPIView):
    queryset = WeatherData.objects.all().order_by('date', 'station_id')
    serializer_class = WeatherDataSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['station_id', 'date']
    ordering_fields = ['station_id', 'date']
    search_fields = ['station_id']

    def get_queryset(self):
        queryset = super().get_queryset()
        return filter_queryset(queryset, self.request)


class WeatherCalculationList(generics.ListAPIView):
    queryset = WeatherCalculation.objects.all().order_by('year', 'station_id')
    serializer_class = WeatherCalculationSerializer
    pagination_class = StandardResultsSetPagination
    filter_backends = [DjangoFilterBackend, filters.OrderingFilter, filters.SearchFilter]
    filterset_fields = ['station_id', 'year']
    ordering_fields = ['station_id', 'year']
    search_fields = ['station_id']

    def get_queryset(self):
        queryset = super().get_queryset()
        return filter_queryset(queryset, self.request)
