import datetime


def fetch_weather_data(city):
    raise NotImplementedError("Implement fetch_weather_data using TDD")


def fetch_forecast(city, days=3):
    raise NotImplementedError("Implement fetch_forecast using TDD")


def get_current_hour():
    return datetime.datetime.now().hour
