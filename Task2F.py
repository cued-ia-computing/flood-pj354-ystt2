from floodsystem.analysis import poly
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
 
 
def generate_dates_levels(s1):
    s1_id = s1.measure_id
    dates_s1, levels = datafetcher.fetch_measure_levels(s1_id,48)
    dates_float = matplotlib.dates.date2num(dates_s1)
    return dates_float, levels
 
 
def run():
    stations = build_station_list()
    station_1 = stations[1]
    id = station_1.measure_id
    a,b,c,d,e = identify_5_top_Rivers()
    list1 = [a,b,c,d,e]
    DataList = [] #Stores dates and levels for each river as a pair
    for i in range(0,5):
        x,y = generate_dates_levels(list1[i])
        DataList.append(x)
        DataList.append(y)
    plot_water_level_with_fit(DataList)
 
run()