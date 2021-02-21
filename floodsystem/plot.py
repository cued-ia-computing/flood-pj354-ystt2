from .analysis import poly
import matplotlib
import matplotlib.pylab as plt
import numpy as np
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels

#for i in range(0,10): #10 days
#        Difference_from_10_days_ago = timedelta(days=i)
 #       date_to_append = Today - Difference_from_10_days_ago
  #      t.append[date_to_append]    
   


def plot_water_level_for_1_station(station):
    date, level = fetch_measure_levels(
    station.measure_id, 24*10)
    date_parameter = round(len(date)/10)
    level_parameter = round(len(level)/10)
    #Getting one reading per 10 days
    t = date[::date_parameter]
    level = level[::level_parameter]
    return t, level 


def plot_water_levels(stations):    
    plt.ylabel("Level of water (Y)")
    plt.xlabel("Date spaced one day apart for 10 days (X)")
    plt.title("Graph of water level against time")
    ListOfWaterLevels = []
    for i in range(0,5):
        x,y = plot_water_level_for_1_station(stations[i])
        plt.plot(x,y, label = stations[i].name)
    plt.legend()
    plt.show()






def Making_X_Y_samelength(x,y):
    x_out = []
    y_out = []
    if len(x) > len(y):
        for i in range(0,len(y) + 1):
            x_out.append(x[i])
            if len(x_out) == len(y):
                return x_out, y
    if len(y) > len(x):
        for i in range(0, len(x) + 1):#
            y_out.append(y[i])
            if len(y_out) == len(x):
                return x, y_out



def plot_water_level_with_fit(Data):
    Rivers = []
    for i in range(0,9):
        temporary = []
        temporary.append(Data[i])
        temporary.append(Data[i+1])
        Rivers.append(temporary)
    for i in range(0,5):
        x,y = Rivers[i]
        if len(x) != len(y):
            x,y = Making_X_Y_samelength(x,y)
        print(len(x), len(y))
        d0, poly_object = poly(x,y,3)
        plt.plot(x, poly_object(x))
        plt.title("This is River " + str(i+1))
        plt.show()
   
        

