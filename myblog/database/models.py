from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class food_table(models.Model):
    #see 3h at video to be dimanic
    Name=models.CharField(max_length=11)
    Carbonhydrates=models.IntegerField()
    Fiber = models.IntegerField()
    Protein = models.IntegerField()
    Fat = models.IntegerField()
    SourceType = models.CharField(max_length=15)

    def __str__(self):
        return self.Name


class DietPlan(models.Model):
    name = models.CharField(max_length=20) # diet plan name 
    date = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(
        'User',
        on_delete=models.CASCADE
        )
    goal = models.CharField() # goal of plan: loss weight, gain weight
    status = models.BooleanField(default=False) # false = unfinished
    carb = models.IntegerField()
    fiber = models.IntegerField()
    protein = models.IntegerField()
    fat = models.IntegerField()
    # optional??
    foods = madels.ManyToManyField(
        food_table, 
        through='GeneratedBy', 
        through_fields=('planID', 'foodID'))

    def __str__(self):
        return self.name

class GeneratedBy(models.Model):
    planID = models.ForeignKey(
        DeitPlan, 
        on_delete=models.CASCADE)
    foodID = models.ForeignKey(
        food_table, 
        on_delete=models.CASCADE)
    amount = models.IntegerField()

# TODO: extend rest-auth user model. NOT finished. 
class UserProfile(models.Model):
    user = models.OneToOneField(User)
    # custom fields for user
    gender = models.CharField(default='undefined')
    height = models.IntegerField()
    age = models.IntegerField()
    cur_weight = models.IntegerField()
    tgt_weight = models.IntegerField()
    is_cook = models.BooleanField()
    plan = models.IntegerField()
    total_cal = models.IntegerField()
    carb = models.IntegerField()
    fib = models.IntegerField()
    protein = models.IntegerField()
    fat = models.IntegerField()

    def __str__(self):
        return self.user


# TODO: Not sure how to set up this table
'''class ChartInfo(models.Model):
    date = models.DateTimeField(default=datetime.now, blank=True)
    username = models.CharField() 
    weight = models.IntegerField()'''


