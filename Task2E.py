from floodsystem.plot import plot_water_levels
from floodsystem import station
from floodsystem.stationdata import build_station_list
from floodsystem import datafetcher
import matplotlib
import numpy as np
import matplotlib.pyplot as plt
from floodsystem.flood import stations_highest_rel_level

def highest_risk():
    ranklist = stations_highest_rel_level(stations, 5)
    return ranklist

def generate_dates_levels(s1):
    s1_id = s1.measure_id
    dates_s1, levels = datafetcher.fetch_measure_levels(s1_id,48)
    dates_float = matplotlib.dates.date2num(dates_s1)
    return dates_float, levels

stations = build_station_list()
station_1 = stations[1]
plot_water_levels(station_1, dates_float, levels)