from dataclasses import dataclass


@dataclass(frozen=True)
class AppConfig:
    city_name: str
    json_file: str
