from django.shortcuts import render
from .api_key import get_news


# Create your views here.

def index(request):
    country = request.GET.get('country', 'us')
    category = request.GET.get('category', 'general')
    page = int(request.GET.get('page', 1))
    query = request.GET.get('q', '')
    
    news = get_news(country=country, category=category, page=page, query=query)
    articles = news.get('articles', [])

    return render(request, 'home/cards.html', {
        'news': articles,
        'country': country,
        'category': category,
        'page': page,
        'has_more': len(articles) == 24 
    })