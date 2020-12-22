import requests
import json
import argparse
import os.path


parser = argparse.ArgumentParser(description = 'Get weather data from wttr.com'
                                               ' and save to a json file',
                                 epilog = 'Enjoy the the weather and the program :)')

parser.add_argument('-city',
                    '--city',
                    action='store',
                    type=str,
                    default='Miskolc',
                    metavar='',
                    help='sets the city for which you want weather data (default Miskolc)')
parser.add_argument('-saveto',
                    '--saveto',
                    action='store',
                    type=str,
                    default='weatherdata',
                    metavar='',
                    help='set the json output file name (default filename: weatherdata)')

args = parser.parse_args()

city_name = args.city
json_file = args.saveto+".json"

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


