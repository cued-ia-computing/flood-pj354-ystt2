from floodsystem.analysis import poly
import matplotlib
import matplotlib.pylab as plt
import numpy as np
from datetime import datetime, timedelta
from floodsystem.datafetcher import fetch_measure_levels

#for i in range(0,10): #10 days
#        Difference_from_10_days_ago = timedelta(days=i)
 #       date_to_append = Today - Difference_from_10_days_ago
  #      t.append[date_to_append]    
   

def filter(t, level):
    for i in level:
        if type(i) == float:
            pass
        else:
            print("There are issues with the data from the servers here, the relevant station has been plotted as y = 0.")
            level = np.zeros(len(t))
    return t, level




def plot_water_level_for_1_station(station):
    date, level = fetch_measure_levels(
    station.measure_id, 24*10)
    date_parameter = round(len(date)/10)
    level_parameter = round(len(level)/10)
    #Getting one reading per 10 days
    t = date[::date_parameter]
    level = level[::level_parameter]
    t, level = filter(t, level)
    return t, level, station.typical_range


def plot_water_levels(stations):    
    plt.ylabel("Level of water (Y)")
    plt.xlabel("Date spaced one day apart for 10 days (X)")
    plt.xticks(rotation=90)
    plt.title("Graph of water level against time")
    for i in range(0,5):
        x,y, trange = plot_water_level_for_1_station(stations[i])
        plt.plot(x,y, label = stations[i].name)
    plt.legend()
    plt.show()









def plot_water_level_with_fit(Data, t_range):
    Rivers = []
    for i in range(0,9):          #creating a list top 9 rivers
        temporary = []
        temporary.append(Data[i])
        temporary.append(Data[i+1])
        Rivers.append(temporary)  
    for i in range(0,5):          #creating 5 graphs for top 5 rivers
        x,y = Rivers[i]
        if len(x) != len(y):       #normalising x and y
            x_out = []
            y_out = []
            if len(x) > len(y):
                for j in range(0,len(y) + 1):
                    x_out.append(x[j])
                    if len(x_out) == len(y):
                        x = x_out
                        break
            if len(y) > len(x):
                for k in range(0, len(x) + 1):
                    y_out.append(y[k])
                    if len(y_out) == len(x):
                        y = y_out
                        break
        d0, poly_object = poly(x,y,4)
        low_range = [t_range[0]] * len(x)
        high_range = [t_range[1]] * len(y)
        plt.plot(x, high_range)
        plt.plot(x, low_range)
        plt.plot(x, poly_object(x))
        print("counter" , i)
        plt.title("This is River with the no." + str(i+1))
        plt.show()
   
        

