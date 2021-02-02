from dataclasses import dataclass

@dataclass
class AppConfig:
    city_name: str
    json_file: str
    url_address: str
