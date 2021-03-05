from floodsystem.plot import plot_water_level_with_fit
from floodsystem.flood import stations_highest_rel_level
from floodsystem.stationdata import build_station_list
from floodsystem.datafetcher import fetch_measure_levels
from floodsystem.stationdata import update_water_levels
from floodsystem.analysis import polyfit
import datetime

def run():
    stations = build_station_list() #intialising
    update_water_levels(stations)
    big = stations_highest_rel_level(stations, 5)
    print(len(big))
    stations_list = []
    for station in big:
       stations_list.append(stations[0])
    print(big)
    dt = 48
    for station in big:
        dates, levels = fetch_measure_levels(station.measure_id, dt)
        if dates==[]:
            print("empty")
        else:
            plot_water_level_with_fit(station,dates,levels,4)

run()