import matplotlib
import datetime
import numpy as np
from datetime import date
import matplotlib.pyplot as plt
from floodsystem.datafetcher import fetch_measure_levels

current_date = date.today()

def polyfit(dates, levels, p):
    time_shift = current_date - datetime.timedelta(days=2)
    y_shift = matplotlib.dates.date2num(time_shift)
    d = matplotlib.dates.date2num(dates)
    shifted_dates = d - y_shift
    p_coeff = np.polyfit(shifted_dates, levels, p) #remember p is the polynomial order parameter!
    poly = np.poly1d(p_coeff)
    return poly, y_shift, shifted_dates

def poly(dates_float, levels, p):   #obsolete. used only for task 2g
    #Finding the coefficients
    p_coeff = np.polyfit(dates_float, levels, p) 
    #Shifting the X axis 
    d0 = max(dates_float)
    #Converting into polynomial
    poly = np.poly1d(p_coeff) # POLYNOMIAL OBJECT HERE!!!! TUNGSTEN YOU MY CUTIE PIE
    tuple_to_return = (d0, poly)
    return tuple_to_return

def generate_dates_levels(s1):
    s1_id = s1.measure_id
    dates_s1, levels = fetch_measure_levels(s1_id,48)
    dates_float = matplotlib.dates.date2num(dates_s1)
    return dates_float, levels, s1.typical_range

def get_poly(station):
    dates_float, levels, trange = generate_dates_levels(station)
    polyfit = poly(dates_float, levels, 4)
    return polyfit