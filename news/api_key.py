import requests
import os

NEWS_API_KEY = os.environ.get('API_KEY')

def get_news(country='us', category='general', page=1, page_size=24, query=''):
    url = (f'https://newsapi.org/v2/top-headlines?country={country}'
           f'&category={category}&page={page}&pageSize={page_size}&apiKey={NEWS_API_KEY}')
    
    if query:
        url = url + f'&q={query}'
    
    response = requests.get(url)
    return response.json()
