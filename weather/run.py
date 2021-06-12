from weather.cli.cli_parser import parse
from weather.core.json_structure import JsonData
from weather.core.appconfig import AppConfig
import weather.core.handle_weather_data as handler
from weather.core.mode_selector import select_mode

def handle():
    args = parse()
    url_address = "http://wttr.in/"+args.city
    app_config = AppConfig(city_name=args.city, json_file=args.saveto, url_address=url_address)
    weather_data = handler.write_webpage_content_in_json_format(app_config.url_address)
    json_dataclass = JsonData(**weather_data)
    select_mode(args.query_mode, args.all ,json_dataclass.__dict__)
    handler.write_content_to_json(app_config.json_file, json_dataclass.__dict__)


if __name__ == "__main__":
    handle()
