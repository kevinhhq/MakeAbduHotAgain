from rest_framework import serializers
from database.models import food_table, DietPlan
from django.contrib.auth.models import User
from django.db.models import Count
from rest_framework import serializers
from rest_auth.models import TokenModel

class FoodSerializer(serializers.ModelSerializer):
    foods_summary = serializers.SerializerMethodField()

    def get_foods_summary(self, obj):
        count_set = food_table.objects.all().values('SourceType').annotate(cnt=Count('SourceType')).order_by('cnt')
        count_dict = {}
        for item in count_set:
            count_dict[item['SourceType']] = item['cnt']
        return count_dict

    class Meta:
        model = food_table
        fields = ('id', 'Name', 'Carbonhydrates','Fiber','Protein','Fat','SourceType', 'foods_summary')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class TokenSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = TokenModel
        fields = ('key', 'user')

class DietPlanSerializer(serializers.ModelSerializer):
    class Meta:
        model = DietPlan
        fields = ('id', 'name', 'date', 
            'user', 'goal', 'status', 
            'carb', 'fiber','protein', 'fat')
    