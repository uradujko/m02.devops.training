import unittest
from unittest.mock import Mock, patch
import weather_service


class TestWeatherService(unittest.TestCase):
    def test_get_weather_success(self):
        with patch("weather_service.api_client.fetch_weather_data") as mock_fetch:
            mock_fetch.return_value = {"city": "London", "temp": 25, "condition": "sunny", "humidity": 50}
            result = weather_service.get_weather("London")
            self.assertEqual(result["temp"], 25)
            self.assertEqual(result["condition"], "sunny")
            mock_fetch.assert_called_once_with("London")

    def test_get_weather_api_error(self):
        with patch("weather_service.api_client.fetch_weather_data") as mock_fetch:
            mock_fetch.side_effect = Exception("API Error")
            with self.assertRaises(Exception):
                weather_service.get_weather("London")

    def test_get_weather_timeout(self):
        with patch("weather_service.api_client.fetch_weather_data") as mock_fetch:
            mock_fetch.side_effect = TimeoutError("Connection timed out")
            with self.assertRaises(TimeoutError):
                weather_service.get_weather("London")

    @patch("weather_service.api_client.fetch_forecast")
    def test_get_forecast_with_patch(self, mock_fetch):
        mock_fetch.return_value = [
            {"day": 1, "temp": 20, "condition": "sunny"},
            {"day": 2, "temp": 22, "condition": "cloudy"},
            {"day": 3, "temp": 18, "condition": "rainy"},
        ]
        result = weather_service.get_forecast("London", 3)
        self.assertEqual(len(result), 3)
        self.assertEqual(result[0]["temp"], 20)
        mock_fetch.assert_called_once_with("London", 3)

    @patch("weather_service.api_client.datetime")
    def test_greeting_morning(self, mock_datetime):
        mock_datetime.datetime.now.return_value.hour = 8
        result = weather_service.get_greeting_based_on_time()
        self.assertEqual(result, "Good morning")

    @patch("weather_service.api_client.datetime")
    def test_greeting_afternoon(self, mock_datetime):
        mock_datetime.datetime.now.return_value.hour = 14
        result = weather_service.get_greeting_based_on_time()
        self.assertEqual(result, "Good afternoon")


if __name__ == "__main__":
    unittest.main()
