from unittest.mock import Mock
from requests.exceptions import URLRequired, Timeout, RequestException, HTTPError
from weather.core.handle_weather_data import get_url_content, write_content_to_json
from pyfakefs.fake_filesystem_unittest import TestCase
import unittest
import os

class MockObject:
    def __init__(self, mock_dict: dict):
        self.text = mock_dict

    def raise_for_status(self):
        pass


class MyTestCase(TestCase):
    def test_get_url_content_with_correct_input(self):
        def mock_dict(*args, **kwargs):
            return MockObject({"weatherCelsius": 1})

        self.assertEqual({"weatherCelsius": 1},
                         get_url_content(mock_dict,
                                         "doNothing"))

    def test_get_url_content_with_empty_response(self):
        def mock_dict(*args, **kwargs):
            return MockObject({})

        with self.assertRaisesRegex(Exception, "Response contains no data"):
            get_url_content(mock_dict,
                            "doNothing")

    def test_get_url_content_with_timeout(self):
        requests = Mock()
        requests.get.side_effect = Timeout
        with self.assertRaisesRegex(Timeout, 'URL request timeout more than \d+ sec'):
            get_url_content(requests.get, "doNothing")

    def test_get_url_content_with_URLRequired(self):
        requests = Mock()
        requests.get.side_effect = URLRequired
        with self.assertRaisesRegex(URLRequired, 'www.invalidAddress.com is an invalid URL'):
            get_url_content(requests.get, "www.invalidAddress.com")

    def test_get_url_content_with_ConnectionError(self):
        requests = Mock()
        requests.get.side_effect = ConnectionError
        with self.assertRaisesRegex(ConnectionError, 'Refused connection or DNS failure etc. occurred'):
            get_url_content(requests.get, "doNothing")

    def test_get_url_content_with_HTTPError(self):
        requests = Mock()
        requests.get.side_effect = HTTPError
        with self.assertRaisesRegex(HTTPError, 'HTTP error: .* occurred'):
            get_url_content(requests.get, "doNothing")

    def test_get_url_content_with_RequestException(self):
        requests = Mock()
        requests.get.side_effect = RequestException
        with self.assertRaisesRegex(RequestException, "There was an ambiguous exception that "
                                                      "occurred while handling request. Error: *"):
            get_url_content(requests.get, "doNothing")

    def test_get_url_content_with_KeyboardInterrupt(self):
        requests = Mock()
        requests.get.side_effect = KeyboardInterrupt
        with self.assertRaisesRegex(KeyboardInterrupt, "Script was interrupted by user"):
            get_url_content(requests.get, "doNothing")

    def test_write_content_to_json(self):
        self.setUpPyfakefs()
        write_content_to_json("fakeFile.json", {'testDict': '1'})
        self.assertTrue(os.path.exists('fakeFile.json'))

        with open("fakeFile.json", 'r') as fileName:
            test_json_format = '{\n    "testDict": "1"\n}'
            self.assertEqual(test_json_format,fileName.read())


if __name__ == '__main__':
    unittest.main()
