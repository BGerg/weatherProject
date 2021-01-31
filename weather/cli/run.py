from weather.cli.cli_parser import parse
from weather.core.json_structure import JsonData
from weather.core.appconfig import AppConfig
from os.path import isfile
from weather.core.handle_weather_data import write_content_to_json, create_basic_json_file, \
    get_webpage_content_in_json_format


def handle(args):
    app_config = AppConfig(args.city, args.saveto)
    if not isfile(app_config.json_file):
        create_basic_json_file(app_config.json_file)
    weather_datas = get_webpage_content_in_json_format(app_config.url_address)
    json_dataclass = JsonData(**weather_datas)
    write_content_to_json(app_config.json_file,json_dataclass.__dict__)


if __name__ == "__main__":
    handle(parse())
