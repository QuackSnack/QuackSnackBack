from django.http import JsonResponse
from back.qs.serializers.article import ArticleSerializer
from back.qs.models.article import Article


def article(request, article_id):

    article = Article.objects.get(pk=article_id)
    serializer = ArticleSerializer(article)

    return JsonResponse(serializer.data)