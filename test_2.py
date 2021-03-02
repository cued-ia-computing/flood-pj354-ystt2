from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.flood import stations_over_threshold, stations_highest_rel_level
import itertools

#2B
def test_stations_over_threshold():
    stations = build_station_list()
    op = stations_over_threshold(stations, 0)
    assert op[0][1] > op[1][1]

def test_stations_highest_rel_level():
    stations = build_station_list()
    op = stations_highest_rel_level(stations, 10)
    assert op[0][1] > op[1][1]
    assert len(op) == 10
