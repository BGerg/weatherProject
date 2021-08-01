def show_current_basics(weather_data: object):
    print(f"Real feel: {weather_data.FeelsLikeC} C°\n"
          f"Local date and time: {weather_data.localObsDateTime}\n"
          f"Temperature: {weather_data.temp_C} C°\n"
          f"Temperature: {weather_data.temp_F} °F\n"
          f"UV index: {weather_data.uvIndex}\n"
          f"Wind speed: {weather_data.windspeedKmph} Kmph\n")


def show_current_all(weather_data: object):
    print(
        f"Real feel: {weather_data.FeelsLikeC} C°\n"
        f"Real feel: {weather_data.FeelsLikeF} °F\n"
        f"Clouds: {weather_data.cloudcover}\n"
        f"Humidity: {weather_data.humidity}\n"
        f"Local date and time: {weather_data.localObsDateTime}\n"
        f"Observation time: {weather_data.observation_time}\n"
        f"precipMM: {weather_data.precipMM} mm\n"
        f"Pressure: {weather_data.pressure} \n"
        f"Temperature: {weather_data.temp_C} C°\n"
        f"Temperature: {weather_data.temp_F} °F\n"
        f"UV index: {weather_data.uvIndex} Fahrenheit\n"
        f"Visibility: {weather_data.visibility}\n"
        f"Weather code: {weather_data.weatherCode}\n"
        f"Weather desc: {weather_data.weatherDesc}\n"
        f"Weather icon url: {weather_data.weatherIconUrl}\n"
        f"winddir16Point: {weather_data.winddir16Point}\n"
        f"winddirDegree {weather_data.winddirDegree}\n"
        f"Wind speed: {weather_data.windspeedKmph} Kmph\n"
        f"Wind speed: {weather_data.windspeedMiles}\n"
    )

def show_choosen_weather_property(weather_data: object):
    pass

