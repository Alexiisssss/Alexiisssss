# 3

# Получить на сайте openweathermap.org  api_key
# Получить текущий индекс качества воздуха в Лондоне и вывести его


# Решение

import requests


def get_air_quality_index(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/air_pollution?lat=51.5074&lon=0.1278&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data


def display_air_quality_index(data):
    if "list" in data:
        air_quality_index = data["list"][0]["main"]["aqi"]
        print(f"Текущий индекс качества воздуха в Лондоне: {air_quality_index}")
    else:
        print("Ошибка при получении данных об индексе качества воздуха.")


def main():
    city = "London"
    api_key = "3f8018e43b0a0cc63a4e2beaac3337a8"
    air_quality_data = get_air_quality_index(city, api_key)
    display_air_quality_index(air_quality_data)


if __name__ == "__main__":
    main()
