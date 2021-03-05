from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import MonitoringStation
from floodsystem.stationdata import build_station_list



#Return slist of inconsistent stations
stations = build_station_list()
Answah = []
for station in stations:
    station.inconsistent_typical_range_stations()
    if station.inconsistent_typical_range_stations() == False:
        Answah.append(station.name)
print(Answah)

