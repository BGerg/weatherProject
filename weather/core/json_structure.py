from dataclasses import dataclass

@dataclass
class WeatherIconUrl:
        value: str

@dataclass
class WeatherDesc:
        value: str

@dataclass
class JsonData:

        FeelsLikeC: int
        FeelsLikeF: int
        cloudcover: int
        humidity: int
        localObsDateTime: str
        observation_time: str
        precipMM: float
        pressure: int
        temp_C: int
        temp_F: int
        uvIndex: int
        visibility: int
        weatherCode: int
        weatherDesc: WeatherDesc
        weatherIconUrl: WeatherIconUrl
        winddir16Point: str
        winddirDegree: int
        windspeedKmph: int
        windspeedMiles: int

