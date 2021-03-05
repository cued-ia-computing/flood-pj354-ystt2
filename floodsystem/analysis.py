import matplotlib
import datetime
import numpy as np
from datetime import date
import matplotlib.pyplot as plt

current_date = date.today()

def polyfit(dates, levels, p):
    time_shift = current_date - datetime.timedelta(days=2)
    y_shift = matplotlib.dates.date2num(time_shift)
    d = matplotlib.dates.date2num(dates)
    shifted_dates = d - y_shift
    p_coeff = np.polyfit(shifted_dates, levels, p) #remember p is the polynomial order parameter!
    poly = np.poly1d(p_coeff)
    return poly, y_shift, shifted_dates

def get_poly(station):
    dates_float, levels, trange = generate_dates_levels(station)
    polyfit = polyfit(dates_float, levels, 4)
    return polyfit