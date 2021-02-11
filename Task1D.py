from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance, stations_with_radius, rivers_with_stations, stations_by_river
import itertools

stations = build_station_list()

print ("first 10 rivers with station, alphabetical: {}".format(list(rivers_with_stations(stations))[0:9]))

d1 = stations_by_river(stations)

for station in ["River Aire", "River Cam", "River Thames"]:
    print ("""
stations by {}: {}""".format(station, d1[station]))