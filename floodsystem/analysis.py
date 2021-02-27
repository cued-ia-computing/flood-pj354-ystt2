import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from floodsystem.geo import stations_by_distance, stations_within_radius, stations_by_river
from . import datafetcher
from floodsystem.stationdata import build_station_list, update_water_levels

def generate_dates_levels(s1):
    s1_id = s1.measure_id
    dates_s1, levels = datafetcher.fetch_measure_levels(s1_id,48)
    dates_float = matplotlib.dates.date2num(dates_s1)
    return dates_float, levels, s1.typical_range

def poly(dates_float, levels, p):
    #Finding the coefficients
    p_coeff = np.polyfit(dates_float, levels, p) 
    #Shifting the X axis 
    d0 = max(dates_float)
    #Converting into polynomial
    poly = np.poly1d(p_coeff) # POLYNOMIAL OBJECT HERE!!!! TUNGSTEN YOU MY CUTIE PIE
    tuple_to_return = (d0, poly)
    return tuple_to_return
