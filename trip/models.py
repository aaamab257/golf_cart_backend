from django.db import models
from users.models import *
from reviews.models import *
 
# Create your models here.


class Trip(models.Model):
    start_location = models.DecimalField(max_digits=2 , decimal_places=2)
    end_location = models.DecimalField(max_digits=2 , decimal_places=2)
    driver = models.ForeignKey(User,on_delete=models.CASCADE)
    review = models.ForeignKey(Reviews, on_delete=models.CASCADE)
    riders = models.IntegerField()
    title = models.CharField(max_length=55)

    def __str__(self):
        return self.title


class GolfCart(models.Model):
    driver = models.ForeignKey(User,on_delete=models.CASCADE)
    review = models.ForeignKey(Reviews, on_delete=models.CASCADE)
    riders = models.IntegerField()
    golf_number = models.CharField(max_length=55)

    def __str__(self):
        return self.golf_number