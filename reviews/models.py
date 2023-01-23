from django.db import models
from users.models import *
# Create your models here.


class Reviews(models.Model):
    review = models.TextField(max_length=500)
    rate = models.IntegerField()
    title = models.CharField(max_length=55)
    user = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.title