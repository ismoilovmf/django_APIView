from django.contrib import admin

from measurement.models import Sensor, Measurement


# Register your models here.
@admin.register(Sensor)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'id']

@admin.register(Measurement)
class SensorAdmin(admin.ModelAdmin):
    list_display = ['sensor', 'created_at']