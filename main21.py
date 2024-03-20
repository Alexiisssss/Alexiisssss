# Работа с API News API
#
# Получить и вывести список последних 10-ти новостей,
# выпущенных информационным агентством BBC;

# pip install newsapi-python

from newsapi import NewsApiClient

# Инициализация клиента News API с вашим ключом API
newsapi = NewsApiClient(api_key='13ccfb80ac5d4749a8f0d4afdc9fd6e0')

# Получение списка последних 10 новостей от BBC
bbc_news = newsapi.get_top_headlines(sources='bbc-news', language='en', page_size=10)

# Вывод заголовков новостей
for article in bbc_news['articles']:
    print(article['title'])
