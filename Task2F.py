from floodsystem.analysis import poly
from floodsystem import station
from floodsystem.stationdata import build_station_list
from floodsystem import datafetcher
import matplotlib
import numpy as np
import matplotlib.pyplot as plt


stations = build_station_list()
station_1 = stations[1]
id = station_1.measure_id
dates, levels = datafetcher.fetch_measure_levels(id,48)
dates_float = matplotlib.dates.date2num(dates)
#print(poly(dates_float, levels, 3))

def identify_5_top_Rivers():
    return stations[1], stations[2], stations[3], stations[4], stations[5]


def generate_dates_levels_(s1,s2,s3,s4,s5):
    s1_id = s1.measure_id
    dates_s1, levels_s1 = datafetcher.fetch_measure_levels(id,48)
    dates_float_s1 = matplotlib.dates.date2num(dates_s1)
    s2_id = s2.measure_id
    dates_s2, levels_s2 = datafetcher.fetch_measure_levels(id,48)
    dates_float_s2 = matplotlib.dates.date2num(dates_s2)
    s3_id = s3.measure_id
    dates_s3, levels_s3 = datafetcher.fetch_measure_levels(id,48)
    dates_float_s3 = matplotlib.dates.date2num(dates_s3)
    s4_id = s4.measure_id
    dates_s4, levels_s4 = datafetcher.fetch_measure_levels(id,48)
    dates_float_s4 = matplotlib.dates.date2num(dates_s4)
    dates_s5, levels_s5 = datafetcher.fetch_measure_levels(id,48)
    dates_float_s5 = matplotlib.dates.date2num(dates_s5)
    return dates_float_s1, levels_s1, dates_float_s2, levels_s2, dates_float_s3, levels_s3, dates_float_s4, levels_s4, dates_float_s5, levels_s5,

    
def polyplot(d1,l1,d2,l2,d3,l3,d4,l4,d5,l5,p):
    #Finding the coefficients
    p_coeff = np.polyfit(d1, l1, p) 
    #Shifting the X axis 
    d0_1 = min(d1)
    new_shifted_float_1 = np.linspace(d0_1, d0_1, num=len(d1))
    shifted_dates_1 = []
    for i in range(0,len(d1)):
        new = d1[i] - new_shifted_float_1[i]
        shifted_dates_1.append(new)
    #Converting into polynomial
    poly_1 = np.poly1d(p_coeff)
    #Now plot

    

        #Finding the coefficients
    p_coeff_2 = np.polyfit(d2, l2, p) 
    #Shifting the X axis 
    d0_2 = min(d2)
    new_shifted_float_2 = np.linspace(d0_2, d0_2, num=len(d2))
    shifted_dates_2 = []
    for i in range(0,len(d2)):
        new = d2[i] - new_shifted_float_2[i]
        shifted_dates_2.append(new)
    #Converting into polynomial
    poly_2 = np.poly1d(p_coeff_2)
    #Now plot

        #Finding the coefficients
    p_coeff_3 = np.polyfit(d3, l3, p) 
    #Shifting the X axis 
    d0_3 = min(d3)
    new_shifted_float_3 = np.linspace(d0_3, d0_3, num=len(d3))
    shifted_dates_3 = []
    for i in range(0,len(d3)):
        new = d3[i] - new_shifted_float_3[i]
        shifted_dates_3.append(new)
    #Converting into polynomial
    poly_3 = np.poly1d(p_coeff_3)
    #Now plot


        #Finding the coefficients
    p_coeff_4 = np.polyfit(d4, l4, p) 
    #Shifting the X axis 
    d0_4 = min(d4)
    new_shifted_float_4 = np.linspace(d0_4, d0_4, num=len(d4))
    shifted_dates_4 = []
    for i in range(0,len(d4)):
        new = d4[i] - new_shifted_float_4[i]
        shifted_dates_4.append(new)
    #Converting into polynomial
    poly_4 = np.poly1d(p_coeff_4)
    #Now plot


        #Finding the coefficients
    p_coeff_5 = np.polyfit(d5, l5, p) 
    #Shifting the X axis 
    d0_5 = min(d5)
    new_shifted_float_5= np.linspace(d0_5, d0_5, num=len(d5))
    shifted_dates_5 = []
    for i in range(0,len(d5)):
        new = d5[i] - new_shifted_float_5[i]
        shifted_dates_5.append(new)
    #Converting into polynomial
    poly_5 = np.poly1d(p_coeff_5)
    #Now plot
    plt.plot(shifted_dates_5, poly_5(d5))
    plt.title("River 5, click X to continue to next River")
    plt.ylabel("Shifted by" + str(d0_5))
    plt.xlabel("Time in Days")
    plt.show()
    plt.plot(shifted_dates_4, poly_4(d4))
    plt.show()
    plt.plot(shifted_dates_3, poly_5(d3))
    plt.show()
    plt.plot(shifted_dates_2, poly_4(d2))
    plt.show()
    plt.plot(shifted_dates_1, poly_5(d1))
    plt.show()



a,b,c,d,e = identify_5_top_Rivers()

d1,l1,d2,l2,d3,l3,d4,l4,d5,l5 = generate_dates_levels_(a,b,c,d,e)

polyplot(d1,l1,d2,l2,d3,l3,d4,l4,d5,l5,3)
