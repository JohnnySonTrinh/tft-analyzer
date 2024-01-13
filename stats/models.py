from django.db import models

class PlayerStats(models.Model):
    player_name = models.CharField(max_length=100)
    wins = models.IntegerField()
    losses = models.IntegerField()
    kills = models.IntegerField()
    deaths = models.IntegerField()
    # ... other fields ...

def __str__(self):
    return self.player_name
