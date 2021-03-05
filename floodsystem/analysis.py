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

def generate_dates_levels(s1):
    s1_id = s1.measure_id
    dates_s1, levels = fetch_measure_levels(s1_id,48)
    dates_float = matplotlib.dates.date2num(dates_s1)
    return dates_float, levels, s1.typical_range

def get_poly(station):
    dates_float, levels, trange = generate_dates_levels(station)
    print (levels)
    print (dates_float)
    a,b,c = polyfit(dates_float, levels, 3)
    return (a,b,c)