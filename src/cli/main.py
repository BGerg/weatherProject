import requests
import json
import os.path



def check_file_exist():
    if not os.path.isfile(json_file):
        create_basic_json_file()

def create_basic_json_file():
    basic_json_file_structure = {"wttr_requests":[]}
    with open(json_file, 'w') as new_file:
        json.dump(basic_json_file_structure, new_file, indent=4)

def read_json_content():
    with open(json_file, 'r') as file:
        original_content = json.load(file)
    return original_content

def set_new_json_content():
    original_content = read_json_content()
    temp = original_content['wttr_requests']
    temp.append(get_wttr_page_content())
    return original_content

def get_wttr_page_content():
    weather_url_address = "http://wttr.in/"+city_name
    response = requests.get(weather_url_address, params=(('format', 'j1'),))
    return json.loads(response.text)

def write_content_to_json(new_content):
    with open(json_file, 'w') as output_file:
        json.dump(new_content, output_file, indent=4)

def main():

    check_file_exist()
    new_file_content = set_new_json_content()
    write_content_to_json(new_file_content)

if __name__ == "__main__":
    main()


