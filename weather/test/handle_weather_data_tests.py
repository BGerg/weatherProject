from weather.core.handle_weather_data import write_content_to_json, write_webpage_content_in_json_format
import unittest
import os

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.mock_dict = {"FeelsLikeC": "5",
                          "FeelsLikeF": "41",
                          "cloudcover": "15",
                          "humidity": "88",
                          }

    def test_write_webpage_content_in_json_format(self):
        self.assertTrue(type(write_webpage_content_in_json_format("http://wttr.in/")) is dict)

    def test_write_content_to_json(self):
        write_content_to_json("testfile.json", self.mock_dict)
        self.assertTrue(os.path.exists("testfile.json"))
        os.remove('testfile.json')

    def test_get_url_content(self):
        pass

