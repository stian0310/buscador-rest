from rest_framework import serializers

from API.models import Search

class SearchSerializer(serializers.ModelSerializer):

  class Meta:
    model = Search
    fields = [
      'id',
      'words',
      'match',
    ]

class SearchCreateUpdateSerializer(serializers.Serializer):
  words = serializers.CharField(max_length=254)

  def save(self, **kwargs):
    try:
      obj = Search.objects.get(words = self.data['words'])
      obj.match += 1
      obj.save()
    except Search.DoesNotExist:
      obj = Search(words = self.data['words'], match = 1)
      obj.save()
