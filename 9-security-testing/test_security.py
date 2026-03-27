import unittest
import requests

BASE_URL = "http://127.0.0.1:5000"


class TestSecurity(unittest.TestCase):
    def test_missing_field_a(self):
        resp = requests.post(f"{BASE_URL}/add", json={"b": 2})
        self.assertEqual(resp.status_code, 400)
        self.assertIn("error", resp.json())

    def test_missing_field_b(self):
        resp = requests.post(f"{BASE_URL}/add", json={"a": 1})
        self.assertEqual(resp.status_code, 400)
        self.assertIn("error", resp.json())

    def test_invalid_data_type(self):
        resp = requests.post(f"{BASE_URL}/add", json={"a": "abc", "b": 2})
        self.assertEqual(resp.status_code, 400)
        self.assertIn("error", resp.json())

    def test_empty_string_value(self):
        resp = requests.post(f"{BASE_URL}/multiply", json={"a": "", "b": 5})
        self.assertEqual(resp.status_code, 400)
        self.assertIn("error", resp.json())

    def test_very_large_number(self):
        resp = requests.post(f"{BASE_URL}/add", json={"a": 1e308, "b": 1e308})
        self.assertIn(resp.status_code, [200, 400])
        self.assertNotEqual(resp.status_code, 500)

    def test_malformed_json(self):
        resp = requests.post(
            f"{BASE_URL}/add",
            data="not json",
            headers={"Content-Type": "application/json"},
        )
        self.assertEqual(resp.status_code, 400)
        self.assertNotEqual(resp.status_code, 500)

    def test_division_by_zero_returns_safe_error(self):
        resp = requests.post(f"{BASE_URL}/divide", json={"a": 10, "b": 0})
        self.assertEqual(resp.status_code, 400)
        data = resp.json()
        self.assertIn("error", data)
        self.assertNotIn("Traceback", str(data))


if __name__ == "__main__":
    unittest.main()
