from django.db import models

from API.models import Search

class Metadata(models.Model):
    search = models.ForeignKey(Search, related_name='metadatas', on_delete=models.CASCADE)
    match = models.PositiveBigIntegerField()
    date = models.DateTimeField()

    class Meta:
        ordering = ('-match', )
