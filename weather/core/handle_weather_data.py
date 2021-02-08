import requests
import json


def write_webpage_content_in_json_format(url_address: str) -> dict:
    url_content = get_url_content(url_address)
    final_data = deserialize_url_content(url_content)
    return final_data


def get_url_content(url_address: str):
    try:
        response = requests.get(url_address, params=(('format', 'j1'),))
        return response
    except requests.exceptions.Timeout:
        print("URL request timeout")
    except requests.URLRequired:
        print("Invalid URL given")
    except requests.ConnectionError:
        print("Connection error occurred.")
    except requests.HTTPError:
        print("HTTP error occurred")
    except requests.RequestException:
        print("There was an ambiguous exception that occurred while handling request.")


def deserialize_url_content(url_content: object):
    deserialized_data = json.loads(url_content.text)['current_condition'][0]
    return deserialized_data


def write_content_to_json(file: str, content: dict):
    with open(file, 'a') as output_file:
        json.dump(content, output_file, indent=4)
