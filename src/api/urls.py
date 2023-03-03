from django.urls import path
from rest_framework import permissions
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from .views import WeatherDataList, WeatherCalculationList

schema_view = get_schema_view(
    openapi.Info(
        title="Weather API",
        default_version='v1',
        description="API for weather data",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('weather/', WeatherDataList.as_view(), name='weather-data-list'),
    path('weather/stats/', WeatherCalculationList.as_view(), name='weather-calculation-list'),
    path('swagger/', schema_view.with_ui('swagger',
        cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
        cache_timeout=0), name='schema-redoc'),
]