# Работа с API OpenWeatherMap
#
# Получить текущую погоду в вашем городе и вывести общее состояние погоды,
# скорость ветра, относительную влажность воздуха, температуру и температуру по ощущениям;


# Решение

# Получите на сайте openweathermap.org ваш api_key

import requests


def get_weather(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data


def display_weather(data):
    if data["cod"] == 200:
        weather_description = data["weather"][0]["description"]
        wind_speed = data["wind"]["speed"]
        humidity = data["main"]["humidity"]
        temperature = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]

        print(f"Общее состояние погоды: {weather_description}")
        print(f"Скорость ветра: {wind_speed} м/с")
        print(f"Относительная влажность воздуха: {humidity}%")
        print(f"Температура: {temperature}°C")
        print(f"Температура по ощущениям: {feels_like}°C")
    else:
        print("Ошибка при получении данных о погоде.")


def main():
    city = "You_City"
    print(f"{city}:")
    api_key = "3f8018e43b0a0cc63a4e2beaac3*****"
    weather_data = get_weather(city, api_key)
    display_weather(weather_data)


if __name__ == "__main__":
    main()
