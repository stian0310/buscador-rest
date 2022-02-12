from django.shortcuts import get_object_or_404, render

from API.models import Search
from API.serializers import SearchSerializer

def index(request):
  searchs = Search.objects.all()
  context = {"searchs": SearchSerializer(searchs, many=True).data}
  return render(request, 'index.html', context)

def detail(request, search_id):
  search = get_object_or_404(Search, pk=search_id)
  return render(request, 'detail.html', {'search': SearchSerializer(search).data})
