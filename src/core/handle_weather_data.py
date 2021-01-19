import requests
import json

def set_new_json_content(file: str, city_to_be_requested: str):
    original_content = read_json_content(file)
    temp = original_content['wttr_requests']
    temp.append(get_wttr_page_content(city_to_be_requested))
    return original_content

def get_wttr_page_content(city_name: str):
    weather_url_address = "http://wttr.in/" + city_name
    response = requests.get(weather_url_address, params=(('format', 'j1'),))
    return json.loads(response.text)

def create_basic_json_file(file: str):
    basic_json_file_structure = {"wttr_requests": []}
    with open(file, 'w') as new_file:
        json.dump(basic_json_file_structure, new_file, indent=4)

def read_json_content(file: str):
    with open(file, 'r') as f:
        return json.load(f)

def write_content_to_json(file: str, content: str):
    with open(file, 'w') as output_file:
        json.dump(content, output_file, indent=4)

