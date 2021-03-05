import matplotlib.pyplot as plt
from .datafetcher import fetch_measure_levels
from .analysis import polyfit

def plot_water_level_with_fit(station, dates, levels, p):
    poly,t,d=polyfit(dates,levels,p)
    pile =[]
    for date1 in d:
        pile.append(poly(date1))
    plt.plot(d, pile)
    plt.plot(d,levels)
    high = [station.typical_range[1]]*len(d)
    low = [station.typical_range[0]]*len(d)
######COSMETICS --> RE CHECK THIS 
    plt.plot(d, high, label='high')
    plt.plot(d, low, label='low')
    plt.xlabel('dates --> nums (w/ shift)')
    plt.ylabel('Water Level (m)')
    plt.xticks(rotation=90)
    plt.title("Graph with a level of shift :" +str(t) +"/n and name of River : " + str(station))
    plt.legend()
    plt.xlim(d[-1],d[0])
    if 1 + 1 == 2:
        plt.show()



def plot_water_levels(station, dates, levels):
    #Plots water levels using ^^^ parameters
    top = [station.typical_range[1]]*len(dates)
    bottom = [station.typical_range[0]]*len(dates)
    plt.plot(dates, levels, label='Recorded Level') 
    plt.plot(dates, top)
    plt.plot(dates, bottom)
    plt.xlabel('The Date (respective)')
    plt.xticks(rotation=45)
    plt.ylabel('W-Level')
    plt.title("The name of the station : " + str(station.name))
    plt.legend()
    plt.show()
