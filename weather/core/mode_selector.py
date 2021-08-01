from weather.core.current_mode import show_current_basics, show_choosen_weather_property, show_current_all


def select_mode(mode: str, switch: str, weather_data: object):
    if mode == 'current' and switch is False:
        show_current_basics(weather_data)
    elif mode == 'current' and switch is True:
        show_current_all(weather_data)

