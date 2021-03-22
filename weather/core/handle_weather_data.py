from typing import Callable
import requests
import json

from requests import URLRequired, RequestException, Timeout, HTTPError


def write_webpage_content_in_json_format(url_address: str) -> dict:
    url_content = get_url_content(requests.get, url_address)
    final_data = deserialize_url_content(url_content)
    return final_data


def get_url_content(get: Callable, url_address: str):
    request_timeout = 5

    try:
        response = get(url_address,
                       params=('format', 'j1'),
                       timeout=request_timeout)
        response.raise_for_status()

        if response.text:  # check response text is empty or not
            return response.text
        else:
            raise Exception("Response contains no data")
    except Timeout:
        raise Timeout(f"URL request timeout more than {request_timeout} sec")
    except URLRequired:
        raise URLRequired(f"{url_address} is an invalid URL")
    except ConnectionError:
        raise ConnectionError("Refused connection or DNS failure etc. occurred")
    except HTTPError as http_err:
        raise HTTPError(f"HTTP error: {http_err}  occurred")
    except RequestException as e:
        raise RequestException(f"There was an ambiguous exception that "
                               f"occurred while handling request. Error: {e} ")


def deserialize_url_content(url_content: object):
    deserialized_data = json.loads(url_content)['current_condition'][0]
    return deserialized_data


def write_content_to_json(file: str, content: dict):
    with open(file, 'a') as output_file:
        json.dump(content, output_file, indent=4)
