from .analysis import poly
import matplotlib
import matplotlib.pylab as plt
import numpy as np
from datetime import datetime



def plot_water_levels(stations, dates, levels):
    t = [datetime(2016, 12, 30), datetime(2016, 12, 31), datetime(2017, 1, 1),
     datetime(2017, 1, 2), datetime(2017, 1, 3), datetime(2017, 1, 4),
     datetime(2017, 1, 5)]
    





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
   
        

