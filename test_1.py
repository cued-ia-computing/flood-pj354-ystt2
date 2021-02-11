from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance, stations_with_radius, rivers_with_stations, stations_by_river, rivers_by_station_number
import itertools

#1B
def test_stations_by_distance():
    p = (52.2053, 0.1218)
    stations = build_station_list()
    out = [('Cambridge Jesus Lock', 0.840237595667494), ('Bin Brook', 2.502277543239629), ("Cambridge Byron's Pool", 4.07204948005424), ('Cambridge Baits Bite', 5.115596582531859), ('Girton', 5.227077565748483), ('Haslingfield Burnt Mill', 7.0443978959918025), ('Oakington', 7.12825901765745), ('Stapleford', 7.265704342799649), ('Comberton', 7.735085060177142)]
    assert stations_by_distance(stations, p)[0:9] == out

#1C
def test_stations_with_radius():
    p = (52.2053, 0.1218)
    stations = build_station_list()
    out = ['Bin Brook', 'Cambridge Baits Bite', "Cambridge Byron's Pool", 'Cambridge Jesus Lock', 'Comberton', 'Dernford', 'Girton', 'Haslingfield Burnt Mill', 'Lode', 'Oakington', 'Stapleford']
    assert stations_with_radius(stations, p, 10) == out

#1D
def test_rivers_with_stations():
    stations = build_station_list()
    for station in stations:
        assert station.river in rivers_with_stations(stations)

#1D
def test_stations_by_river():
    stations = build_station_list()
    out = ['Cam', 'Cambridge', 'Cambridge Baits Bite', 'Cambridge Jesus Lock', 'Dernford', 'Great Chesterford', 'Weston Bampfylde']
    assert stations_by_river(stations)['River Cam'] == out

#1E
def test_rivers_by_station_number():
    stations = build_station_list()
    out = [('River Thames', 55), ('River Avon', 32), ('River Great Ouse', 30)]
    assert rivers_by_station_number(stations, 3) == out