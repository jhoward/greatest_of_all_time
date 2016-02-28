from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Quarterback(models.Model):
    name = models.CharField(max_length=200)
    passing_yards = models.PositiveIntegerField()
    passing_touchdowns = models.PositiveIntegerField()
    passing_attempts = models.PositiveIntegerField()
    passing_completions = models.PositiveIntegerField()


    def __str__(self):
        return self.name
