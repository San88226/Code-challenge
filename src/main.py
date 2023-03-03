import csv
import glob
from datetime import datetime
from django.db import models
from api.models import WeatherData, WeatherCalculation

def ingest_weather_data():
    """
    Ingest weather data from TSV files.
    """
    folder_path = "../wx_data"
    file_list = glob.glob(f"{folder_path}/*.txt")
    data = []
    print("Weather data insertion started at ", datetime.now())
    WeatherData.objects.all().delete()
    
    for file_path in file_list:
        with open(file_path, "r", encoding="utf8") as file:
            tsv_reader = csv.reader(file, delimiter="\t")
            for row in tsv_reader:
                date = datetime.strptime(str(row[0]), "%Y%m%d").date()
                max_temp = float(row[1]) / 10 if row[1] != "-9999" else None
                min_temp = float(row[2]) / 10 if row[2] != "-9999" else None
                precipitation = float(row[3]) / 10 if row[3] != "-9999" else None
                station_id = file_path.split("/")[-1].split(".")[0]
                data.append(WeatherData(date=date, max_temp=max_temp, min_temp=min_temp,
                                        precipitation=precipitation, station_id=station_id))           
    WeatherData.objects.bulk_create(data, ignore_conflicts=True, batch_size=1000)
    print(f"{len(data)} weather data records inserted at {datetime.now()}.")

def calculate_weather_stats():
    """
    Calculate weather statistics for each year and station.
    """
    print("weather statistics records started at ", datetime.now())
    WeatherCalculation.objects.all().delete()
    weather_data = WeatherData.objects.exclude(max_temp=None, min_temp=None, precipitation=None)
    station_ids = weather_data.order_by().values_list("station_id", flat=True).distinct()
    years = range(weather_data.aggregate(min_year=models.Min("date__year"))["min_year"],
                    weather_data.aggregate(max_year=models.Max("date__year"))["max_year"] + 1)
    
    for year in years:
        for station_id in station_ids:
            data_for_station = weather_data.filter(station_id=station_id, date__year=year)
            avg_max_temp = data_for_station.aggregate(models.Avg("max_temp"))["max_temp__avg"]
            avg_min_temp = data_for_station.aggregate(models.Avg("min_temp"))["min_temp__avg"]
            total_precipitation = data_for_station.aggregate(models.Sum("precipitation"))["precipitation__sum"]
            stats = WeatherCalculation(year=year, station_id=station_id, avg_max_temp=avg_max_temp,
                                        avg_min_temp=avg_min_temp, total_precipitation=total_precipitation)
            stats.save()
    print(f"{len(station_ids) * len(years)} weather statistics records inserted at {datetime.now()}.")

ingest_weather_data()
calculate_weather_stats()
