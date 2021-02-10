import requests
import json


def write_webpage_content_in_json_format(url_address: str) -> dict:
    url_content = get_url_content(url_address)
    final_data = deserialize_url_content(url_content)
    return final_data


def get_url_content(url_address: str):
    request_timeout = 5
    try:
        response = requests.get(url_address, params=(('format', 'j1'),), timeout=request_timeout)
        response.raise_for_status()

        if not response.text:
            return response
        else:
            print("Response contains no data")
    except requests.exceptions.Timeout:
        raise TimeoutError(f"URL request timeout more than {request_timeout} sec")
    except requests.URLRequired:
        raise Exception(f"{url_address} is invalid URL")
    except requests.ConnectionError:
        raise Exception("Refused connection or DNS failure etc. occures")
    except requests.HTTPError as http_err:
        raise Exception(f"HTTP error occurred {http_err}")
    except requests.RequestException as e:
        raise Exception(f"{e} There was an ambiguous exception that occurred while handling request.")


def deserialize_url_content(url_content: object):
    deserialized_data = json.loads(url_content.text)['current_condition'][0]
    return deserialized_data


def write_content_to_json(file: str, content: dict):
    with open(file, 'a') as output_file:
        json.dump(content, output_file, indent=4)
