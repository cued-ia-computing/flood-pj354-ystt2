import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from datafetcher import fetch_measure_levels
from station import MonitoringStation
from stationdata import build_station_list


stations = build_station_list()
station_1 = stations[3]
id = station_1.measure_id
dates, levels = fetch_measure_levels(id,200)
#converting datetime into float
dates_float = matplotlib.dates.date2num(dates)
#plotting the thing now

def poly(dates_float, levels, p):
    #Finding the coefficients
    p_coeff = np.polyfit(dates_float, levels, p) 
    #Shifting the X axis 
    _shifted = min(dates_float)
    new_shifted_float = np.linspace(_shifted, _shifted, num=len(dates_float))
    shifted = []
    for i in range(0,len(dates_float)):
        new = dates_float[i] - new_shifted_float[i]
        shifted.append(new)
    #Converting into polynomial
    poly = np.poly1d(p_coeff)
    #Now plot
    plt.plot(shifted, poly(dates_float))
    plt.show()



poly(dates_float, levels, 3)