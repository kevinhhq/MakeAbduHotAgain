from rest_framework import serializers
from database.models import food_table
from django.contrib.auth.models import User
from rest_framework import serializers
from rest_auth.models import TokenModel

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = food_table
        fields = ('id', 'Name', 'Carbonhydrates','Fiber','Protein','Fat','SourceType')

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'email')

class TokenSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = TokenModel
        fields = ('key', 'user')