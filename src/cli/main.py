from os.path import isfile

from src.cli.cli_parser import parse
from src.core.appconfig import AppConfig
from src.core.handle_weather_data import write_content_to_json, append_new_content_to_old, \
    create_basic_json_file_structure


def handle(args):

    app_config = AppConfig(args.city, args.saveto)
    if not isfile(app_config.json_file):
        create_basic_json_file_structure(app_config.json_file)
    new_file_content = append_new_content_to_old(app_config.json_file, app_config.url_address)
    write_content_to_json(app_config.json_file, new_file_content)


if __name__ == "__main__":
    handle(parse())

