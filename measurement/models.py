from django.db import models

# TODO: опишите модели датчика (Sensor) и измерения (Measurement)
class Sensor(models.Model):
    name = models.CharField(unique=True, max_length=25, verbose_name="Называние")
    description = models.CharField(max_length=50, verbose_name='Локация')
    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'
    def __str__(self):
        return f'{self.name}'


class Measurement(models.Model):
    sensor= models.ForeignKey(Sensor, on_delete=models.CASCADE, related_name='measurements', )
    temperature = models.FloatField(verbose_name='Температура')
    created_at = models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name = "Измерение"
        verbose_name_plural = "Измерении"
    def __str__(self):
        return f'{self.sensor.description}'