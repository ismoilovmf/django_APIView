from django.urls import path

from measurement.views import ListCreateAPIView, RetrieveUpdateAPIView, sensors

urlpatterns = [
    path('v1/sensor/<int:pk>/', sensors),
    path('v1/sensors/', ListCreateAPIView.as_view()),
    path('v1/sensors/<int:pk>/', ListCreateAPIView.as_view()),
    path('v1/measurements/', RetrieveUpdateAPIView.as_view()),
    path('v1/measurements/<int:pk>/', RetrieveUpdateAPIView.as_view()),
]

