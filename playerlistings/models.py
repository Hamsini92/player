from django.db import models

# Create your models here.

class Intuit(models.Model):
    player_id = models.CharField(primary_key=True, max_length=1500)
    birth_country = models.CharField(max_length=1500, blank=True,default=False)
    birth_state = models.CharField(max_length=1500, blank=True,default=False)
    birth_city = models.CharField(max_length=1500, blank=True,default=False)
    birthYear = models.IntegerField(null=True)
    birthMonth = models.IntegerField(null=True)
    birthDay = models.IntegerField(null=True)
    deathYear = models.IntegerField(null=True)
    deathMonth = models.IntegerField(null=True)
    deathDay = models.IntegerField(null=True)
    deathCountry = models.CharField(max_length=1500, blank=True)
    deathState = models.CharField(max_length=1500, blank=True)
    deathCity = models.CharField(max_length=1500, blank=True)
    nameFirst = models.CharField(max_length=1500, blank=True)
    nameLast = models.CharField(max_length=1500, blank=True)
    nameGiven = models.CharField(max_length=1500, blank=True)
    weight = models.IntegerField(null=True, blank=True)
    height = models.IntegerField(null=True, blank=True)
    bats = models.CharField(max_length=1500, null=True, default=False)
    throws = models.CharField(max_length=1500, blank=True, default=False)
    debut = models.DateTimeField(auto_now_add=True, null=True)
    finalGame = models.DateTimeField(auto_now_add=True, null=True)
    retroID = models.CharField(max_length=1500, blank=True, default=False)
    bbrefID = models.CharField(max_length=1500, blank=True, default=False)

