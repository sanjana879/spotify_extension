from django.db import models
from django import forms
SEARCH_OPTIONS = (
    ('playlist'),
    ('album'),
    ('artist'),
)

class Results(models.Model):
    name = models.CharField(max_length=30)
    artist = models.CharField(max_length=30)
    #img = models.CharField(max_length=100)

class Emotion(models.Model):
    name = models.CharField(max_length=30)
    count = models.PositiveIntegerField()