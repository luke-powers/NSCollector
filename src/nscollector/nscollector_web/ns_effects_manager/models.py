# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Effect(models.Model):
    effect_name = models.CharField(max_length=255)
    # Set of value ranges and the change for that range. before, after, change.
    # For incoming effect changes, if the change value is == replace
    # stored before with the smallest before and the after with the
    # largest after.
    effect_ranges = [[0, 0, 0]]


class EffectsChangesLog(models.Model):
    after = models.IntegerField()
    before = models.IntegerField()
    change = models.IntegerField()
    effect = models.ForeignKey(Effect, on_delete=models.PROTECT)
    issue = models.IntegerField()


class EffectPreferences(models.Model):
    effect = models.ForeignKey(Effect, on_delete=models.PROTECT)
    nation = models.ForeignKey('Nation', on_delete=models.CASCADE)
    weight = models.IntegerField(default=0)


class Nation(models.Model):
    nation_name = models.CharField(max_length=255)
