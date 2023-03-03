from django.db import models

# Create your models here.


class WeatherData(models.Model):
    station_id = models.CharField(max_length=20)
    date = models.DateField()
    max_temp = models.DecimalField(
        max_digits=6, decimal_places=2, null=True)
    min_temp = models.DecimalField(
        max_digits=6, decimal_places=2, null=True)
    precipitation = models.DecimalField(
        max_digits=6, decimal_places=2, null=True)

    def __str__(self):
        return f"{self.date} ({self.station_id})"

    class Meta:
        unique_together = ('date', 'station_id')


class WeatherCalculation(models.Model):
    year = models.IntegerField()
    station_id = models.CharField(max_length=50)
    avg_max_temp = models.DecimalField(
        max_digits=6, decimal_places=2, null=True)
    avg_min_temp = models.DecimalField(
        max_digits=6, decimal_places=2, null=True)
    total_precipitation = models.DecimalField(
        max_digits=6, decimal_places=2, null=True)

    def __str__(self):
        return f"{self.year} ({self.station_id})"

    class Meta:
        unique_together = ('year', 'station_id')