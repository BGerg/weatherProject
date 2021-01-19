
class AppConfig:
    __instance = None

    def __init__(self, city, json_file):
        if AppConfig.__instance is None:
            AppConfig.__instance = self

            self.city_name = city
            self.json_file = json_file
            self.url_address = "http://wttr.in/" + self.city_name
        else:
            raise Exception("You cannot create another Appconfig class")

    @staticmethod
    def getInstance():
        if AppConfig.__instance == None:
            AppConfig()
        return AppConfig.__instance





