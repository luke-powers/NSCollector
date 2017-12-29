# -*- coding: utf-8 -*-
from django.db import models


class CensusChangesLog(models.Model):
    current = models.IntegerField()
    before = models.IntegerField()
    id = models.AutoField(primary_key=True, default=0)
    issue = models.IntegerField()


class Census(models.Model):
    name = models.CharField(max_length=255)
    values = models.ForeignKey(CensusChangesLog, on_delete=models.PROTECT)


class CensusPreferences(models.Model):
    census = models.ForeignKey(Census, on_delete=models.PROTECT)
    nation = models.ForeignKey('Nation', on_delete=models.CASCADE)
    weight = models.IntegerField(default=0)


class Nation(models.Model):
    nation_name = models.CharField(max_length=255)
