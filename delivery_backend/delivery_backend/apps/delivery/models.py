from django.db import models


class QueryResponse(models.Model):
    location_from = models.CharField(max_length=200)
    location_to = models.CharField(max_length=200)
    distance = models.IntegerField()


class QueryRequest(models.Model):
    location_from = models.CharField(max_length=200)
    location_to = models.CharField(max_length=200)
