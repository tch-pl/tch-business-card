from django.db import models


class Personal(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    birth_date = models.DateTimeField('date published')
    