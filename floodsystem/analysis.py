import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def poly(dates_float, levels, p):
    #Finding the coefficients
    p_coeff = np.polyfit(dates_float, levels, p) 
    #Shifting the X axis 
    d0 = min(dates_float)
    new_shifted_float = np.linspace(d0, d0, num=len(dates_float))
    shifted_dates = []
    for i in range(0,len(dates_float)):
        new = dates_float[i] - new_shifted_float[i]
        shifted_dates.append(new)
    #Converting into polynomial
    poly = np.poly1d(p_coeff)
    #Now plot
    plt.plot(shifted_dates, poly(dates_float))
    plt.show()



