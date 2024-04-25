# Работа с API OpenWeatherMap
# Получить погоду в вашем городе на следующий день.

# Решение


import requests
from datetime import datetime, timedelta


def get_weather_forecast(city, api_key):
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    return data


def get_tomorrows_forecast(forecast_data):
    tomorrow = datetime.now() + timedelta(days=1)
    tomorrow_date = tomorrow.strftime("%Y-%m-%d")

    for forecast in forecast_data["list"]:
        if forecast["dt_txt"].split()[0] == tomorrow_date:
            return forecast
    return None


def display_weather_forecast(forecast):
    if forecast:
        weather_description = forecast["weather"][0]["description"]
        wind_speed = forecast["wind"]["speed"]
        humidity = forecast["main"]["humidity"]
        temperature = forecast["main"]["temp"]
        feels_like = forecast["main"]["feels_like"]

        print(f"Прогноз погоды на завтра:")
        print(f"Общее состояние погоды: {weather_description}")
        print(f"Скорость ветра: {wind_speed} м/с")
        print(f"Относительная влажность воздуха: {humidity}%")
        print(f"Температура: {temperature}°C")
        print(f"Температура по ощущениям: {feels_like}°C")
    else:
        print("Прогноз на завтра отсутствует.")


def main():
    city = "Челябинск"
    print(f"{city}:")
    api_key = "3f8018e43b0a0cc63a4e2beaac3337a8"
    forecast_data = get_weather_forecast(city, api_key)
    tomorrows_forecast = get_tomorrows_forecast(forecast_data)
    display_weather_forecast(tomorrows_forecast)


if __name__ == "__main__":
    main()
