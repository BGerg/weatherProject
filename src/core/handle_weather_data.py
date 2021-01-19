import requests
import json

def append_new_content_to_old(file: str, url_address: str):
    content = read_json_file_content(file)
    temp = content['wttr_requests']
    temp.append(get_webpage_content_in_json_format(url_address))
    return content

def get_webpage_content_in_json_format(url_address: str):
    response = requests.get(url_address, params=(('format', 'j1'),))
    return json.loads(response.text)

def create_basic_json_file_structure(file: str):
    basic_json_file_structure = {"wttr_requests": []}
    with open(file, 'w') as new_file:
        json.dump(basic_json_file_structure, new_file, indent=4)

def read_json_file_content(file: str):
    with open(file, 'r') as f:
        return json.load(f)

def write_content_to_json(file: str, content: str):
    with open(file, 'w') as output_file:
        json.dump(content, output_file, indent=4)

