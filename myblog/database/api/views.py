from database.models import food_table
from .serializers import FoodSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class FoodViewSet(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    queryset = food_table.objects.all()
