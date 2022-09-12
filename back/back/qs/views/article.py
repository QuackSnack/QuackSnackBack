from django.http import JsonResponse
from back.qs.serializers.article import ArticleSerializer
from back.qs.models.article import Article


def all_article(request):

  articles = Article.objects.all()
  serializer = ArticleSerializer(articles, many=True)

  return JsonResponse({'data': serializer.data})


def single_article(request, article_id):

  article = Article.objects.get(pk=article_id)
  serializer = ArticleSerializer(article)

  return JsonResponse(serializer.data)
