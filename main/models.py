from django.db import models
from django.contrib.auth.models import User

class File(models.Model):
    complain_type = (
        ('water','Water Resources'),
        ('electricity','Electricity'),
    )

    user_name = models.CharField(User, max_length = 20)
    complain_type = models.CharField(max_length = 20, choices = complain_type)
    title = models.CharField(max_length = 50)
    mobile_no = models.IntegerField()

    def __str__(self):
        return self.title

