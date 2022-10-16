from measurement.models import Measurement, Sensor
from measurement.serializers import MeasurementSerializer, SensorSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

@api_view(['GET', ])
def sensors(request, *args, **kwargs):
    if not (pk := kwargs.get('pk', None)):
        return Response({"detail": "Неверные данные."})
    try:
        sensor = Sensor.objects.get(pk=pk)
        a=0
    except:
        return Response({"detail": "Запись не найдена."})
    ser = SensorSerializer(sensor)
    return Response(ser.data)

class ListCreateAPIView(APIView):
    def get(self, request):
        sensor = Sensor.objects.values('id', 'name', 'description')
        ser = SensorSerializer(sensor, many=True)
        return Response(ser.data)

    def post(self, request):
        serializer = SensorSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'POST': serializer.data})

    def put(self, request, *args, **kwargs):
        if not (pk := kwargs.get('pk', None)):
            return Response({"detail": "Неверные данные."})
        try:
            instance = Sensor.objects.get(pk=pk)
        except:
            return Response({"detail": "Запись не найдена."})
        serializer = SensorSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'PUT': serializer.data})

class RetrieveUpdateAPIView(APIView):
    def get(self, request):
        measurements = Measurement.objects.all()
        ser = MeasurementSerializer(measurements, many=True)
        return Response(ser.data)

    def post(self, request):
        # TODO Добавить измерение. Указываются ID датчика и температура.
        serializer = MeasurementSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'POST': serializer.data})
        pass