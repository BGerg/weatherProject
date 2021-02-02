import requests
import json

def get_webpage_content_in_json_format(url_address: str) -> dict:
    response = requests.get(url_address, params=(('format', 'j1'),))
    return json.loads(response.text)['current_condition'][0]

def create_basic_json_file(file: str):
    with open(file, 'w') as new_file:
        pass

def write_content_to_json(file: str, content: str):
    with open(file, 'a') as output_file:
        json.dump(content, output_file, indent=4)


