
class AppConfig:
    __instance = None

    def __init__(self, city, json_file):
        if AppConfig.__instance is None:
            AppConfig.__instance = self

            self.city_name = city
            self.json_file = json_file
            self.url_prefix = "http://wttr.in/"
            self.url_address = self.url_prefix + self.city_name

        else:
            AppConfig.__instance


