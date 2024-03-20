# Работа с API News API


#pip install newsapi-python
#Перейдите на сайт News API: https://newsapi.org/
#Нажмите на кнопку "Get API Key" в верхнем правом углу страницы.

# Инициализация клиента News API с вашим ключом API
newsapi = NewsApiClient(api_key='YOUR_API_KEY')

# Получение списка последних 10 новостей от BBC
bbc_news = newsapi.get_top_headlines(sources='bbc-news', language='en', page_size=10)

# Вывод заголовков новостей
for article in bbc_news['articles']:
    print(article['title'])
