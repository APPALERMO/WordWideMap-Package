from WorldWideMap import WorldWideMap
from WorldWideMap.converter import Converter
from WorldWideMap.gui import GuiMappa

# Rome Coordinates: 41°53′57.12″ | 12°32′42.00″
converter = Converter()
lat = converter.degrees_to_decimal(41, 53, 57.12)
lon = converter.degrees_to_decimal(12, 32, 42.00)
print("{}, {}".format(lat, lon))

latg = converter.decimal_to_degrees(lat, show_degrees=True)
long = converter.decimal_to_degrees(lon)
print(latg, long)

# Get City Name from Coordinates
wwm = WorldWideMap(lat, lon)
city_name = wwm.cityName()
print("The City is: {}".format(city_name))

# Get Coordinates From City Name
wwm = WorldWideMap()
Dubai = wwm.nameToCoordinates("Dubai", istuple=True)
print("The Dubai Coordinates is: {}".format(Dubai))

# Let's calculate the distance Roma - Milano
Milano = (45.463688, 9.188141)
Roma = (41.902782, 12.496366)

wwm = WorldWideMap()
distance = wwm.distanceCalculate(Milano, Roma)
print("The distance Milano - Roma is: {} Km".format(distance))
metres = converter.kilometres_to_metres(distance)
print("The distance Milano - Roma, in metres, is: {} m".format(metres))

# WorldWideMap(Dubai[0], Dubai[1]).openMap("Mappa di Dubai")

GuiMappa.start()
