Описание задания. Используя пример веб-скрейпинга практической части урока, 
проведите скрейпинг сайта с новостями из сферы ИИ (https://2051.vision/category/ii/), 
выведите на экран заголовки новостей.

from bs4 import BeautifulSoup
import requests

for page_num in range(1, 16):
    url = f"https://2051.vision/category/ii/page/{page_num}"
    html = requests.get(url).text
    soup = BeautifulSoup(html, 'html5lib')

    print(f"Страница {page_num}:")
    for h3 in soup.find_all('h3'):
        print(h3.text.strip())
    print("\n")
