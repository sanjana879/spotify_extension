from django.db import models
from django import forms

SEARCH_OPTIONS = (
    ('LAB', 'labor'),
    ('CAR', 'cars'),
    ('TRU', 'trucks'),
    ('WRI', 'writing'),
)
# Create your models here.
class SearchOptions(models.Model):
    option = models.CharField(max_length=30, choices=SEARCH_OPTIONS)
        #models.CharField(max_length=30, choices=SEARCH_OPTIONS)