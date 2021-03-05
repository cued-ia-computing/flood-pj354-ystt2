from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance, stations_with_radius, rivers_with_stations, stations_by_river
import itertools

stations = build_station_list()
p = (52.2053, 0.1218)  # coords of cambridge

print("closest 10 stations from cambridge: {}".format(stations_by_distance(stations, p)[0:10]))
print("furthest 10 stations from cambridge: {}".format(stations_by_distance(stations, p)[-10:]))