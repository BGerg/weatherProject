from weather.cli.cli_parser import parse
from weather.core.json_structure import JsonData
from weather.core.appconfig import AppConfig
from os.path import isfile
from weather.core.handle_weather_data import write_content_to_json, get_webpage_content_in_json_format
import sys


def handle(args):
    url_address = "http://wttr.in/"+args.city
    app_config = AppConfig(city_name=args.city, json_file=args.saveto, url_address=url_address)
    weather_datas = get_webpage_content_in_json_format(app_config.url_address)
    json_dataclass = JsonData(**weather_datas)
    write_content_to_json(app_config.json_file, json_dataclass.__dict__)


if __name__ == "__main__":
    handle(parse())
