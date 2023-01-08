import os
import time
import folium
import requests
import webbrowser


class WorldWideMap():
    def __init__(self, lat=None, lon=None):
        self.lat = lat
        self.lon = lon

    def cityName(self) -> str:
        url = f"https://nominatim.openstreetmap.org/reverse?format=jsonv2&lat={self.lat}&lon={self.lon}"

        response = requests.get(url)
        data = response.json()
        self.name_local = data["display_name"]

        return self.name_local

    def nameToCoordinates(self, city_name, more_info=False, istuple=False):
        self.city_name = city_name
        url = f"https://nominatim.openstreetmap.org/search?q={self.city_name}&format=json"
        response = requests.get(url)

        data = response.json()
        data = data[0]

        self.lat = round(float(data["lat"]), 4)
        self.lon = round(float(data["lon"]), 4)

        if istuple:
            return (self.lat, self.lon)

        if more_info:
            self.complete_name = data["display_name"]
            return "{} {} | {}".format(self.lat, self.lon, self.complete_name)

        else:
            return "{} {}".format(self.lat, self.lon)

    def distanceCalculate(self, coordinatesStartPoint: tuple, coordinatesEndPoint: tuple):
        self.point1 = coordinatesStartPoint
        self.point2 = coordinatesEndPoint

        url = "https://dev.virtualearth.net/REST/v1/Routes/DistanceMatrix"

        params = {
            "origins": f"{self.point1[0]},{self.point1[1]}",
            "destinations": f"{self.point2[0]},{self.point2[1]}",
            "travelMode": "driving",
            "key": "An4rnDTS6ca4vLZlK0nDFgjxPnCUuRhVqsbg7QotgZXgo1b5Xa8QXHZU1S_Rc3Gf",
        }

        response = requests.get(url, params=params)

        if response.status_code == 200:
            # Estrazione della distanza in chilometri dalla risposta dell'API
            distance = response.json()["resourceSets"][0]["resources"][0]["results"][0]["travelDistance"]
            return distance
        else:
            return f"{response.status_code}: {response.text}"

    def openWebMap(self):
        url = f"https://www.openstreetmap.org/#map=18/{self.lat}/{self.lon}"
        webbrowser.open(url)

    def openMap(self, map_name, keep=False):
        self.map_name = f"{map_name}.html"
        mappa = folium.Map(location=[self.lat, self.lon], zoom_start=11)
        mappa.save(self.map_name)
        webbrowser.open(self.map_name)

        if keep:
            pass
        else:
            time.sleep(1)
            os.remove(self.map_name)


class Converter():
    def decimal_to_degrees(self, number, show_degrees=False):
        self.degrees = int(number)
        self.minutes = int((number - self.degrees) * 60)
        self.seconds = (number - self.degrees - self.minutes / 60) * 3600

        if show_degrees:
            return "{}° {}′ {}″".format(self.degrees, self.minutes, round(self.seconds, 2))
        else:
            self.seconds = round(self.seconds, 2)
            return self.degrees, self.minutes, self.seconds

    def degrees_to_decimal(self, degrees, minutes, seconds):
        self.decimal = degrees + minutes / 60 + seconds / 3600

        return self.decimal

    def metres_to_kilometres(self, metres):

        self.metres = metres
        self.kilometres = self.metres / 1000

        return self.kilometres

    def kilometres_to_metres(self, kilometres):

        self.kilometres = kilometres
        self.metres = self.kilometres * 1000

        return self.metres
