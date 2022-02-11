import requests

from django.shortcuts import render
from django.http import HttpResponse
from django.template.loader import render_to_string

from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import action

from API.models import Search
from API.serializers import SearchSerializer, SearchCreateUpdateSerializer

from weasyprint import HTML
from weasyprint.fonts import FontConfiguration


class SearchView( mixins.ListModelMixin,
    viewsets.GenericViewSet):

    queryset = Search.objects.all()
    serializer_class = SearchSerializer
    pagination_class =  LimitOffsetPagination

    def get_serializer_class(self):
        if self.action in ['create', 'update', 'partial_update']:
            return SearchCreateUpdateSerializer
        else:
            return self.serializer_class

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)        
        d = self.makerequest(serializer.data['words'])
        serializer.save()
        return Response(d, status=status.HTTP_201_CREATED)

    def makerequest(self, word):
        URL = "https://en.wikipedia.org/w/api.php"
        SEARCHPAGE = word
        PARAMS = { "action": "query", "format": "json", "list": "search", "srsearch": SEARCHPAGE}
        R = requests.get(url=URL, params=PARAMS)
        DATA = R.json()
        return DATA

    @action(detail=False, methods=['get',])
    def report(self, request):
        searchs = Search.objects.all()
        context = {"searchs": searchs}
        html = render_to_string("reports.html", context)
        response = HttpResponse(content_type="application/pdf")
        font_config = FontConfiguration()
        HTML(string=html).write_pdf(response, font_config=font_config)
        return response