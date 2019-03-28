from database.models import food_table, DietPlan
from .serializers import FoodSerializer, DietPlanSerializer
from rest_framework import viewsets
from rest_framework.response import Response

class FoodViewSet(viewsets.ModelViewSet):
    serializer_class = FoodSerializer
    queryset = food_table.objects.all()

class DietPlanViewSet(viewsets.ModelViewSet):
    serializer_class = DietPlanSerializer
    queryset = DietPlan.objects.all()