from django.contrib import admin

# Register your models here.
from .models import food_table, DietPlan, GeneratedBy, UserProfile
admin.site.register(food_table)
admin.site.register(DietPlan)
admin.site.register(GeneratedBy)
admin.site.register(UserProfile)