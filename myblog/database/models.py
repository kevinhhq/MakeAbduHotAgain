from django.db import models

# Create your models here.
class food_table(models.Model):
    #see 3h at video to be dimanic
    Name=models.CharField(max_length=11)
    Carbonhydrates=models.IntegerField()
    Fiber = models.IntegerField()
    Protein = models.IntegerField()
    Fat = models.IntegerField()


