from weather.cli.cli_parser import parse
from weather.run import handle

if __name__ == "__main__":
    handle(parse())
