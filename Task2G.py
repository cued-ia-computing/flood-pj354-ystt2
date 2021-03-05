from floodsystem.flood import stations_over_threshold
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.flood import stations_over_threshold, stations_highest_rel_level
from floodsystem.analysis2 import get_towns, sampling, generate_dates_levels, get_poly, critA, critB, critC, critD, sum_criteria, spatial_average, rate

def run():
    stations = build_station_list()
    update_water_levels(stations)
    
    # demo1: get townlist with co-ords
    t1 = get_towns(stations)

    for town in t1:
        if town[0] == "Bedford":  # note: "Cambridge" is not used as an example because of Cambridge in Gloucestershire (indistinguishable without external database)
            print ("Town with coordinates: {}".format(town))  # the co-ords acquired by averaging coordinates of stations with station.name == "Bedford"

    # demo2: get sample of stations given a certain town 
            sample = sampling(stations, town)
            print ("Stations associated (with 10km) with town: {}".format(sample))
    
    # demo3: computing each of the criteria scores for a specific station
            for station in stations:
                if station.name == sample[0]:
                    print("--- Example station: {} ---".format(station.name))
                    print("critA: {}".format(critA(station)))
                    print("critB: {}".format(critB(station)))
                    print("critC: {}".format(critC(station)))
                    print("critD: {}".format(critD(station)))

    # demo4: summing up the criteria scores to get raw scores from each station
            station_scores = sum_criteria(sample, town, stations)
            print("each tuple contains (station.name, distance from town centre, raw score): {}".format(station_scores))
    # demo5: spatial average of raw scores of sampled stations around the town
            spatial_avg = spatial_average(station_scores)
            print("spatial average: {}".format(spatial_avg))
    # demo6: converting spatial average into rating for a specific town — severe, high, moderate, low
            print("""
                    -------
            town: {}
            the current for rating is: 
            {}
                    -------""".format(town,rate(spatial_avg)))
        

if __name__ == "__main__":
    print("*** Task 2A: CUED Part IA Flood Warning System ***")
    run()