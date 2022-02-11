from django.db import models

class Search(models.Model):
    words = models.CharField(max_length=254, unique=True)
    match = models.PositiveBigIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-match', )
