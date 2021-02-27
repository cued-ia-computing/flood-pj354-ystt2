from floodsystem.analysis import poly, generate_dates_levels
from floodsystem.plot import plot_water_level_with_fit
from floodsystem import station
from floodsystem.stationdata import build_station_list
from floodsystem import datafetcher
from floodsystem.flood import stations_highest_rel_level
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
 
def identify_5_top_Rivers():
    stations = build_station_list()
    risklist = stations_highest_rel_level(stations, 5)
    return risklist[3], risklist[4], risklist[2], risklist[1], risklist[0]
 
 
 
def run():
    stations = build_station_list()
    station_1 = stations[1]
    id = station_1.measure_id
    a,b,c,d,e = identify_5_top_Rivers()
    list1 = [a,b,c,d,e]
    DataList = [] #Stores dates and levels for each river as a pair
    rangelist = []
    for i in range(0,5):
        x,y, t_range = generate_dates_levels(list1[i])
        rangelist.append(t_range[1] - t_range[0])
        DataList.append(x)
        DataList.append(y)

    plot_water_level_with_fit(DataList, rangelist)
 
run()