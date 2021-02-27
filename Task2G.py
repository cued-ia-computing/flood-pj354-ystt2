from floodsystem.flood import stations_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_over_threshold, stations_highest_rel_level
from floodsystem.analysis import get_towns, sampling

def run():
    stations = build_station_list()
    update_water_levels(stations)
    
    # demo1: get townlist with co-ords
    t1 = get_towns(stations)

    for town in t1:
        if town[0] == "Bedford":  # note: "Cambridge" is not used as an example because of Cambridge in Gloucestershire (indistinguishable without external database)
            print ("Town with coordinates: {}".format(town))  # the co-ords acquired by averaging coordinates of stations with station.name == "Bedford"

    # demo2: get sample of stations given a certain town
            print (sampling(stations, town))
    
    # demo3: computing each of the criteria scores
            print (sampling)
            #print("critA score:{}".format(critA(stations, station)))
            


if __name__ == "__main__":
    print("*** Task 2A: CUED Part IA Flood Warning System ***")
    run()