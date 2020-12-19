import requests
import json


def get_wttr_page_content():
    response = requests.get('http://wttr.in/Miskolc', params=(('format', 'j1'),))
    return response

def write_content_to_json_file(response):
    with open('weatherdatas.json', 'a') as json_file:
        json.dump(response.json(), json_file, indent=6)



def main():
    weather_Data = get_wttr_page_content()
    write_content_to_json_file(weather_Data)

if __name__ == "__main__":
    main()