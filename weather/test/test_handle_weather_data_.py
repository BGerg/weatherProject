from unittest.mock import Mock
from unittest.mock import patch
from requests.exceptions import URLRequired, Timeout, RequestException, HTTPError
import requests

from weather.core.handle_weather_data import get_url_content
import unittest



class MyTestCase(unittest.TestCase):

    def test_get_url_content_with_correct_input(self):
        class MockObject:
            def __init__(self):
                self.text = {"weatherCelsious": 1}

            def raise_for_status(self):
                pass

        def mock_dict(*args, **kwargs):
            return MockObject()

        self.assertEqual({"weatherCelsious": 1},
                         get_url_content(mock_dict,
                                         "doNothing"))


    def test_get_url_content_with_empty_response(self):
        class MockObject:
            def __init__(self):
                self.text = {}

            def raise_for_status(self):
                pass

        def mock_dict(*args, **kwargs):
            return MockObject()

        with self.assertRaises(Exception):
            get_url_content(mock_dict,
                            "doNothing")

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
        with self.assertRaisesRegex(ConnectionError, 'Refused connection or DNS failure etc. occured'):
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


if __name__ == '__main__':
    unittest.main()