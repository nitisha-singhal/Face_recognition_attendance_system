from rest_framework import generics
from ..models import Schedule
from .serializers import ScheduleSerializer
from rest_framework.response import Response

class DayScheduleView (generics.ListAPIView) :
    queryset = 