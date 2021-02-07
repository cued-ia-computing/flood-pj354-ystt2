from floodsystem.flood import stations_over_threshold
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_over_threshold

def run():
    stations = build_station_list()
    
    update_water_levels(stations)
    relatives = []
    names = [
        'Bourton Dickler', 'Surfleet Sluice', 'Gaw Bridge', 'Hemingford',
        'Swindon'
    ]
    # part a: demonstrating fetch of relative levels
    for station in stations:
        if station.name in names:
            relative = station.relative_water_level()
            relatives.append((station.name, relative))
    print (""" --
relative levels of selected stations: {}
-- """.format(relatives))

    #part b: demonstrating acquisition of list of over-tolerance stations and their relative levels
    print ("list of stations over relative level of 1: {}".format(stations_over_threshold(stations, 1)[0:9]))

if __name__ == "__main__":
    print("*** Task 2A: CUED Part IA Flood Warning System ***")
    run()