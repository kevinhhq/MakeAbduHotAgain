from rest_framework import serializers
from database.models import food_table

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = food_table
        fields = ('id', 'Name', 'Carbonhydrates','Fiber','Protein','Fat')