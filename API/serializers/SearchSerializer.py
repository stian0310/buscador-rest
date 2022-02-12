from django.utils import timezone
from datetime import timedelta

from rest_framework import serializers

from API.models import Search,Metadata
from API.serializers import MetadataSerializer

class SearchSerializer(serializers.ModelSerializer):
  metadatas = MetadataSerializer(many=True, read_only=True)

  class Meta:
    model = Search
    fields = [
      'id',
      'words',
      'totalmatch',
      'metadatas',
    ]

class SearchCreateUpdateSerializer(serializers.Serializer):
  words = serializers.CharField(max_length=254)

  def save(self, **kwargs):
    ti = timezone.now()
    # ti = timezone.now()-timedelta(days=1)
    try:
      obj = Search.objects.get(words = self.data['words'])
      obj.totalmatch += 1
      obj.save()
      md = Metadata.objects.filter(
        search = obj.id,
        date__year = ti.year,
        date__month = ti.month,
        date__day = ti.day
        ).first()
      if md == None:
        Metadata.objects.create(
          search = obj,
          match = 1,
          date = str(ti),
          )
      else:
        md.match += 1
        md.save()
    except Search.DoesNotExist:
      obj = Search(words = self.data['words'], totalmatch = 1)
      obj.save()
      md = Metadata.objects.create(
        search = obj,
        match = 1,
        date = str(ti),
        )
