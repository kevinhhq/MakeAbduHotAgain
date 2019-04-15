from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now


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
    date = models.DateTimeField(default=now, blank=True)
    user = models.ForeignKey(
        'UserProfile',
        on_delete=models.CASCADE
        )
    GOAL_CHOICES = ['Lose Fat', 'Keep', 'Gain Weight/Muscle']
    goal = models.CharField(
        max_length=20, 
        choices=[(i, i) for i in GOAL_CHOICES], 
        default='Keep') 
    status = models.BooleanField(default=False)
    carb = models.IntegerField()
    fiber = models.IntegerField()
    protein = models.IntegerField()
    fat = models.IntegerField()
    # optional??
    foods = models.ManyToManyField(
        food_table, 
        through='GeneratedBy', 
        through_fields=('plan', 'food'))

    def __str__(self):
        return self.name

class GeneratedBy(models.Model):
    plan = models.ForeignKey(
        DietPlan, 
        on_delete=models.CASCADE)
    food = models.ForeignKey(
        food_table, 
        on_delete=models.CASCADE)
    amount = models.IntegerField()

    def __str__(self):
        return self.plan.name+ "." + self.food.Name

# TODO: extend rest-auth user model. NOT finished. 
class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = user.name
    GENDER_CHOICES = ['Male', 'Female', 'Others']
    gender = models.CharField(
        max_length=10, 
        choices=[(i, i) for i in GENDER_CHOICES], 
        default='Others')
    LOSEFAT = 'LF'
    GAINMUSCLE= 'GM'
    TRANSFORM = 'TF'
    MY_GOAL_CHOICE = (
        (LOSEFAT, 'Lose Fat'),             #actual value, human-readable name
        (GAINMUSCLE, 'Gain Muscle'),
        (TRANSFORM, 'Transform'),
    )
    my_goal = models.CharField(
        max_length=2,
        choices=MY_GOAL_CHOICE,
        default=TRANSFORM,
    )
    VERYACTIVE = 'VA'
    ACTIVE = 'AC'
    NOTACTIVE = 'NA'
    ACTIVITY_CHOICE = (
        (VERYACTIVE, 'Very Active'),
        (ACTIVE, 'Active'),
        (NOTACTIVE, ' Not Active'),
    )
    activity = models.CharField(
        max_length=2,
        choices=ACTIVITY_CHOICE,
        default=ACTIVE,
    )
    height = models.IntegerField(blank=True)
    age = models.IntegerField(blank=True)
    weight = models.IntegerField(blank=True)
    ## is it a one-to-one relation???

    def __str__(self):
        return self.user.username


# TODO: Not sure how to set up this table
'''class ChartInfo(models.Model):
    date = models.DateTimeField(default=datetime.now, blank=True)
    username = models.CharField() 
    weight = models.IntegerField()'''


