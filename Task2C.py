from floodsystem.flood import stations_over_threshold
from floodsystem.stationdata import build_station_list
from floodsystem.stationdata import update_water_levels
from floodsystem.flood import stations_over_threshold, stations_highest_rel_level

def run():
    stations = build_station_list()
    update_water_levels(stations)
    print ("-- 10 stations with highest risk, with relative levels --")
    l1 = stations_highest_rel_level(stations, 10)
    for i in range(0,9):
        print ("{}: {}".format(l1[i][0], l1[i][1]))

if __name__ == "__main__":
    print("*** Task 2A: CUED Part IA Flood Warning System ***")
    run()