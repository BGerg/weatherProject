import requests
import json
import sys


def get_webpage_content_in_json_format(url_address: str) -> dict:
    try:
        response = requests.get(url_address, params=(('format', 'j1'),))
        return json.loads(response.text)['current_condition'][0]
    except requests.exceptions.RequestException:
        print("URL not available")
        sys.exit()

def write_content_to_json(file: str, content: str):
    with open(file, 'a') as output_file:
        json.dump(content, output_file, indent=4)
