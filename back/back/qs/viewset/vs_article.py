from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet

from back.qs.models.article import Article
from back.qs.serializers.article import ArticleSerializerFull


class ArticleViewSet(ViewSet):
    def list(self, request):
        queryset = Article.objects.all()
        serializer = ArticleSerializerFull(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = Article.objects.all()
        article = get_object_or_404(queryset, pk=pk)
        serializer = ArticleSerializerFull(article)
        return Response(serializer.data)