from weather.core.current_mode import *


def select_mode(mode: str, switch: str, weather_data: dict):
    if mode == 'current' and switch == False:
        show_current_basics(weather_data)
    elif mode == 'current' and switch == True:
        show_current_all(weather_data)

