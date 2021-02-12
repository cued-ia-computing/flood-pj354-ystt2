from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance, stations_with_radius, rivers_with_stations, stations_by_river
import itertools

stations = build_station_list()
p = (52.2053, 0.1218)  # coords of cambridge
r = 10 #10 km around

print ("stations witin 10km of cambridge: {}".format(stations_with_radius(stations, p, 10)))