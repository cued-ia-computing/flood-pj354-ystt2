import matplotlib
import matplotlib.pyplot as plt
import numpy as np


def poly(dates_float, levels, p):
    #Finding the coefficients
    p_coeff = np.polyfit(dates_float, levels, p) 
    #Shifting the X axis 
    d0 = min(dates_float)
    #Converting into polynomial
    poly = np.poly1d(p_coeff) # POLYNOMIAL OBJECT HERE!!!! TUNGSTEN YOU MY CUTIE PIE
    tuple_to_return = [d0, poly]
    return tuple_to_return

def differentiate_and_value(y, x): #where y is the function you want to differentiate. Y must be a np.polynomial TYPE!!! 
#where x is the point at where you want the value of the gradient to be!
    dy_dx = np.polyder(y)
    value = np.polyval(dy_dx, x)
    return value






