from floodsystem.plot import plot_water_levels
from floodsystem import station, datafetcher, flood
from floodsystem.stationdata import build_station_list, update_water_levels
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from floodsystem.flood import stations_highest_rel_level
#from floodsystem.datafetcher import update_water_levels
from floodsystem.datafetcher import fetch_measure_levels


def run():
    stations = build_station_list() #INTIALISING
    update_water_levels(stations)
    bigger_than_last_time = stations_highest_rel_level(stations, 5)
    to_plotter_than_last_time = []
    for station in bigger_than_last_time:
        to_plotter_than_last_time.append(stations[0])
    for station in to_plotter_than_last_time:
        dates, levels = fetch_measure_levels(station.measure_id, 10*24)
        plot_water_levels(station, dates, levels)


run()