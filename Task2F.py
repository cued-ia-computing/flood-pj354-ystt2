from floodsystem.analysis import poly
from floodsystem.plot import plot_water_level_with_fit
from floodsystem import station
from floodsystem.stationdata import build_station_list
from floodsystem import datafetcher
import matplotlib
import numpy as np
import matplotlib.pyplot as plt


stations = build_station_list()
station_1 = stations[1]
id = station_1.measure_id
dates, levels = datafetcher.fetch_measure_levels(id,48)
dates_float = matplotlib.dates.date2num(dates)



def identify_5_top_Rivers():
    return stations[1], stations[2], stations[3], stations[4], stations[5]


def generate_dates_levels_(s1):
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
    for i in range(1,5):
        x,y = generate_dates_levels_(list1[i])
        plot_water_level_with_fit(x,y,3)

run()



