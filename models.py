from django.db import models

class SensorData(models.Model):
    temperature = models.FloatField()
    humidity = models.FloatField()
    nitrogen = models.FloatField()
    phosphorus = models.FloatField()
    potassium = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Sensor Data {self.id} - {self.timestamp}"

class CropRecommendation(models.Model):
    crop_name = models.CharField(max_length=100)
    probability = models.FloatField()
    sensor_data = models.ForeignKey(SensorData, on_delete=models.CASCADE)

    def __str__(self):
        return self.crop_name
