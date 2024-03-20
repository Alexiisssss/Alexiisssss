# Работа с API News API

# Получить и вывести список 5-ти последних новостей связанных с ИИ.

# pip install newsapi-python
# Перейдите на сайт News API: https://newsapi.org/
# Нажмите на кнопку "Get API Key" в верхнем правом углу страницы.

from newsapi import NewsApiClient

# Инициализация клиента News API с вашим ключом API
newsapi = NewsApiClient(api_key='13ccfb80ac5d4749a8f0d4afdc9fd6e0')

# Получение списка последних новостей, связанных с искусственным интеллектом
ai_news = newsapi.get_everything(q='искусственный интеллект', language='ru', page_size=5)

# Вывод заголовков новостей
for article in ai_news['articles']:
    print(article['title'])
