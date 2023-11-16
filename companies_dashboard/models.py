# Create your models here.
from django.db import models


# class Member(models.Model):
#     # Define your fields here
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     # ...other fields...
#
#     def __str__(self):
#         return f"{self.first_name} {self.last_name}"

#
class Company(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    industry = models.CharField(max_length=50)
    founded = models.DateField()
    website = models.URLField()

    def __str__(self):
        return self.name
