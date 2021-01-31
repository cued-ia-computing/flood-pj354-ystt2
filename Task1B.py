from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

stations = build_station_list()
p = (52.1810, 0.0932)  # grantchester

floodsystem.geo.stations_by_distance(stations, p)