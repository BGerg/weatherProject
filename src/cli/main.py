import requests
import json

def read_json_content():
    with open('weatherdatas.json') as json_file:
        original_content = json.load(json_file)
    return original_content

def set_new_json_content():
    original_content = read_json_content()
    temp = original_content['wttr_requests']
    temp.append(get_wttr_page_content())
    return original_content

def get_wttr_page_content():
    response = requests.get('http://wttr.in/Miskolc', params=(('format', 'j1'),))
    return json.loads(response.text)

def write_content_to_json(response):
    with open('weatherdatas.json', 'w') as json_file:
        json.dump(response, json_file, indent=4)

def main():

    data = set_new_json_content()
    write_content_to_json(data)

if __name__ == "__main__":
    main()


