from cli.cli_parser import parse
import heandle_weather_data

def main(parse):

    check_file_exist()
    new_file_content = set_new_json_content()
    write_content_to_json(new_file_content)

if __name__ == "__main__":
    main(parse)


