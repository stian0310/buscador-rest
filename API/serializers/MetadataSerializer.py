from rest_framework import serializers

from API.models import Metadata

class MetadataSerializer(serializers.ModelSerializer):

  class Meta:
    model = Metadata
    fields = [
      'date',
      'match',
    ]