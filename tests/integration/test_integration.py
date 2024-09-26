import unittest
import requests

class TestIntegration(unittest.TestCase):
    def test_api_status(self):
        response = requests.get('http://localhost:8000/')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
