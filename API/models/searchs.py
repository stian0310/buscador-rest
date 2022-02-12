from django.db import models

class Search(models.Model):
    words = models.CharField(max_length=254, unique=True)
    totalmatch = models.PositiveBigIntegerField()

    class Meta:
        ordering = ('-totalmatch', )
