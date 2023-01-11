import os
import time
import json
import folium
import requests
import webbrowser

api_key = "An4rnDTS6ca4vLZlK0nDFgjxPnCUuRhVqsbg7QotgZXgo1b5Xa8QXHZU1S_Rc3Gf"

class WorldWideMap():
    def __init__(self, lat=None, lon=None):
        self.lat = lat
        self.lon = lon

    def cityName(self) -> str:
        url = f"http://dev.virtualearth.net/REST/v1/Locations/{self.lat},{self.lon}?key={api_key}"

        response = requests.get(url)
        data = json.loads(response.text)
        self.name_local = data["resourceSets"][0]["resources"][0]["address"]["locality"]

        return self.name_local

    def nameToCoordinates(self, name_of_city, more_info=False, istuple=False):
        url = f"http://dev.virtualearth.net/REST/v1/Locations?q={name_of_city}&key={api_key}"

        response = requests.get(url)
        data = json.loads(response.text)
        latitude = data["resourceSets"][0]["resources"][0]["point"]["coordinates"][0]
        longitude = data["resourceSets"][0]["resources"][0]["point"]["coordinates"][1]

        self.lat = round(float(latitude), 4)
        self.lon = round(float(longitude), 4)

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


    def openMap(self, map_name, keep=False):
        map_name = f"{map_name}.html"
        mappa = folium.Map(location=[self.lat, self.lon], zoom_start=11)
        folium.Marker(location=[self.lat, self.lon], popup=WorldWideMap(self.lat, self.lon).cityName()).add_to(mappa)
        mappa.save(map_name)
        webbrowser.open(map_name)

        if keep:
            pass
        else:
            time.sleep(1)
            os.remove(map_name)
