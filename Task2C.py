from floodsystem.flood import stations_level_over_threshold
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_level_over_threshold, stations_highest_rel_level

def run():
    stations = build_station_list()
    update_water_levels(stations)
    l1 = stations_highest_rel_level(stations, 10)
    print ("-- 10 stations with highest risk, with relative levels --")
    for i in range(0, len(l1)):
        print ("{}: {}".format(l1[i].name, l1[i].relative_water_level()))

if __name__ == "__main__":
    print("*** Task 2A: CUED Part IA Flood Warning System ***")
    run()