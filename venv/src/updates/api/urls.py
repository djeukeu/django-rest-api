from django.urls import path, include
from .views import (UpdateModelListAPIView, UpdateModelAPIView)

urlpatterns = [
    path('', UpdateModelListAPIView.as_view()),
    path('<id>/', UpdateModelAPIView.as_view()),
]
