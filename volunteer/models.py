from django.db import models
from users.models import *
# Create your models here.


class Volunteer(models.Model):
    name = models.CharField(max_length=55)
    email = models.ForeignKey(User,on_delete=models.CASCADE)
    student_id = models.CharField(max_length=15)
    phone = models.CharField(max_length=15)
    license = models.ImageField()
    health_status = models.BooleanField(default=True)
    accepted = models.BooleanField(default=False)

    def __str__(self):
        return self.name