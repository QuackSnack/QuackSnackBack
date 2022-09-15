import json
from django.http import JsonResponse
from back.qs.serializers.article import ArticleSerializer
from back.qs.models.article import Article
from django.views.decorators.csrf import requires_csrf_token, csrf_exempt


def get_article(request, article_id=None):
  if request.method == 'GET':
    if article_id is None:
      try:
        article = Article.objects.all()
        serializer = ArticleSerializer(article, many=True)
      except Article.DoesNotExist:
        return JsonResponse({'message': "article not found"}, status=400)
    elif isinstance(article_id, int):
      try:
        article = Article.objects.get(pk=article_id)
        serializer = ArticleSerializer(article)
      except Article.DoesNotExist:
        return JsonResponse({'message': "article not found"}, status=400)
    return JsonResponse({'data': serializer.data})
  return JsonResponse({'message': "Wrong type of request"}, status=400)


@csrf_exempt
def create_article(request):
  if request.method == 'POST':
    if request.user.role == 1:
      parameters = json.loads(request.body)
      article = Article(name=parameters['name'],
                        image=parameters['image'],
                        description=parameters['description'],
                        price=parameters['price'],
                        tag=parameters['tag'])
      article.save()
      return JsonResponse({'message': "Article created"})
    return JsonResponse({'message': "The user isn't a restaurant"}, status=400)
  return JsonResponse({'message': "Wrong type of request"}, status=400)
