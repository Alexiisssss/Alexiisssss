# Работа с API News API

# Получить и вывести список информационных агентств, публикующих новости на испанском языке;


#pip install newsapi-python
#Перейдите на сайт News API: https://newsapi.org/
#Нажмите на кнопку "Get API Key" в верхнем правом углу страницы.

from newsapi import NewsApiClient

# Инициализация клиента News API с вашим ключом API
newsapi = NewsApiClient(api_key='13ccfb80ac5d4749a8f0d4afdc9fd6e0')

# Получение списка информационных агентств на испанском языке
spanish_sources = newsapi.get_sources(language='es')

# Вывод списка информационных агентств
for source in spanish_sources['sources']:
    print(source['name'])
