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




def plot_water_level_for_1_station(station): #Making all the data for each station nice and plottable so matplotlib doesn't die
    date, level = fetch_measure_levels(
    station.measure_id, 24*10)
    date_parameter = round(len(date)/10)
    level_parameter = round(len(level)/10) # Data Slicing and rounding^^^
    #Getting one reading per 10 days
    t = date[::date_parameter]
    level = level[::level_parameter]
    t, level = filter(t, level)
    return t, level, station.typical_range #Returnign Typical Range is for 2F.


def plot_water_levels(stations):    
    plt.ylabel("Level of water (Y)")
    plt.xlabel("Date spaced one day apart for 10 days (X)")
    plt.xticks(rotation=90) #Neater.
    plt.title("Graph of water level against time")
    for i in range(0,5):
        x,y, trange = plot_water_level_for_1_station(stations[i])  #Trange not really needed.
        plt.plot(x,y, label = stations[i].name)
    plt.legend()
    plt.show() 






def Making_X_Y_samelength(x,y): #Not used anymore.
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
                return x, y_out, trange
        



def plot_water_level_with_fit(Data, t_range):
    Rivers = []
    for i in range(0,9):          #Making the Top 5 Riskiest River data in a nicer format to manipulate
        temporary = []
        temporary.append(Data[i])
        temporary.append(Data[i+1])
        Rivers.append(temporary)  
    for i in range(0,5):          #creating 5 graphs for top 5 rivers
        x,y = Rivers[i]
        if len(x) != len(y):       #making sure the len(River_Level) is the same as len(Dates)
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
        plt.plot(x, poly_object(x))
        #Here t_range[i] is the difference in range for the relevant, included in the plot of the respective river.
        plt.title("This is River with the no." + str(i+1) + " greatest levels of Water. It's range is : " + str(t_range[i])) 
        plt.show() #1 Plot for each river for better visiblity and scale
   
        

