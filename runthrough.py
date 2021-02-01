from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance, stations_with_radius, rivers_with_stations, stations_by_river
import itertools

stations = build_station_list()
p = (52.1810, 0.0932)  # coords of grantchester

print("closest 10 stations from grantchester: {}".format(stations_by_distance(stations, p)[0:9]))

print ("stations witin 10km of grantchester: {}".format(stations_with_radius(stations, p, 10)))

print ("first 10 rivers with station, alphabetical: {}".format(list(rivers_with_stations(stations))[0:9]))

d1 = stations_by_river(stations)
d2 = dict(itertools.islice(d1.items(), 4))   

print ("stations for each river: {}".format(d2))