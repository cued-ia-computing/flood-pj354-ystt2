from floodsystem.geo import rivers_by_station_number
from floodsystem.stationdata import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.geo import generate_rivers


stations = build_station_list()
print(rivers_by_station_number(stations, 9))