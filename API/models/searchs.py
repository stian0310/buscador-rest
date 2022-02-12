from django.db import models

class Search(models.Model):
    words = models.CharField(max_length=254, unique=True)
    totalmatch = models.PositiveBigIntegerField()

    def __str__(self):
        return f'{self.words} - tm: {self.totalmatch}'


    class Meta:
        ordering = ('-totalmatch', )

