from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance, stations_with_radius, rivers_with_stations, stations_by_river, rivers_by_station_number
import itertools

#1B
def test_stations_by_distance():
    p = (52.1810, 0.0932)
    stations = build_station_list()
    out = [("Cambridge Byron's Pool", 1.1409229626226685), ('Bin Brook', 1.8453396671939495), ('Haslingfield Burnt Mill', 3.726837709841944), ('Cambridge Jesus Lock', 4.010985535348231), ('Comberton', 5.060586051188609), ('Stapleford', 5.7283910687962685), ('Dernford', 6.145145756795305), ('Girton', 7.0547787706321055), ('Cambridge Baits Bite', 8.40767768506205)]
    assert stations_by_distance(stations, p)[0:9] == out

#1C
def test_stations_with_radius():
    p = (52.1810, 0.0932)
    stations = build_station_list()
    out = ["Cambridge Byron's Pool", 'Bin Brook', 'Haslingfield Burnt Mill', 'Cambridge Jesus Lock', 'Comberton', 'Stapleford', 'Dernford', 'Girton', 'Cambridge Baits Bite', 'Oakington', 'Babraham']
    assert stations_with_radius(stations, p, 10) == out

#1D
def test_rivers_with_stations():
    stations = build_station_list()
    for station in stations:
        assert station.river in rivers_with_stations(stations)

#1D
def test_stations_by_river():
    stations = build_station_list()
    out = ['Hemingford', 'Ravenstone Mill Sluice', 'St Ives', 'Welney Causeway', 'Newport Pagnell (Cemetery)', 'Sutton Gault', 'St Neots', 'Stony Stratford', 'Offord', 'Bromham', 'Olney', 'Brackley', 'Godmanchester', 'Bedford', 'Castle Mill (Bedford)', 'Cardington', 'Brampton Sluice', 'Roxton', 'Brownshill', 'Newport Pagnell', 'Earith', 'Thornborough', 'Buckingham', 'Houghton', 'Ely', 'Haversham', 'Sharnbrook', 'Turvey', 'Passenham', 'Eaton Socon']
    assert stations_by_river(stations)['River Great Ouse'] == out

#1E
def test_rivers_by_station_number():
    stations = build_station_list()
    out = [('River Thames', 55), ('River Avon', 32), ('River Great Ouse', 30)]
    assert rivers_by_station_number(stations, 3) == out