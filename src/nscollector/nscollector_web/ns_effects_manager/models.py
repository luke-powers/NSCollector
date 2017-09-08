# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Census(models.Model):
    census_id = models.IntegerField()
    census_name = models.CharField(max_length=255)
    # Set of value ranges and the change for that range. before, after, change.
    # For incoming census changes, if the change value is == replace
    # stored before with the smallest before and the after with the
    # largest after.
    census_ranges = [[0, 0, 0]]


class CensussChangesLog(models.Model):
    after = models.IntegerField()
    before = models.IntegerField()
    change = models.IntegerField()
    census = models.ForeignKey(Census, on_delete=models.PROTECT)
    issue = models.IntegerField()


class CensusPreferences(models.Model):
    census = models.ForeignKey(Census, on_delete=models.PROTECT)
    nation = models.ForeignKey('Nation', on_delete=models.CASCADE)
    weight = models.IntegerField(default=0)


class Nation(models.Model):
    nation_name = models.CharField(max_length=255)
