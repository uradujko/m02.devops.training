import datetime


def fetch_weather_data(city):
    return {
        "city": city,
        "temp": 20,
        "condition": "sunny",
        "humidity": 60,
    }


def fetch_forecast(city, days=3):
    return [{"day": i + 1, "temp": 20 + i, "condition": "sunny"} for i in range(days)]


def get_current_hour():
    return datetime.datetime.now().hour
