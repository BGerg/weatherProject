from cli_parser import parse
from src.core.handle_weather_data import set_new_json_content, get_wttr_page_content, read_json_content



def main(parse):

    app_config = AppConfig(args.city_name, args.json_file)
    if not isfile(app_config.json_file):
        create_basic_json_file(app_config.json_file)
    new_file_content = set_new_json_content(app_config.json_file, app_config.city_name)
    write_content_to_json(app_config.json_file, new_file_content)

if __name__ == "__main__":
    main(parse)


