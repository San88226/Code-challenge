from django.contrib import admin

from .models import WeatherData,WeatherCalculation


class WeatherDataAdmin(admin.ModelAdmin):
    list_display=('station_id','date','max_temp','min_temp','precipitation')
admin.site.register(WeatherData,WeatherDataAdmin)

class WeatherCalculationAdmin(admin.ModelAdmin):
    list_display=('year','station_id','avg_max_temp','avg_min_temp','total_precipitation')
admin.site.register(WeatherCalculation,WeatherCalculationAdmin)    
# Register your models here.
