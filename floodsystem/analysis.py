import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def poly(dates_float, levels, p):
    #Finding the coefficients
    p_coeff = np.polyfit(dates_float, levels, p) 
    #Shifting the X axis 
    d0 = min(dates_float)
    #Converting into polynomial
    poly = np.poly1d(p_coeff)
    tuple_to_return = [d0, poly]
    return tuple_to_return



