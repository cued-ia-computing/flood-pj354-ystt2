import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from haversine import haversine, Unit
from floodsystem.geo import stations_by_distance, stations_within_radius


def poly(dates_float, levels, p):
    #Finding the coefficients
    p_coeff = np.polyfit(dates_float, levels, p) 
    #Shifting the X axis 
    d0 = min(dates_float)
    #Converting into polynomial
    poly = np.poly1d(p_coeff)
    tuple_to_return = [d0, poly]
    return tuple_to_return

def get_towns(stations):
    def towns_with_stations(stations):
        towns = set([])
        for station in stations:
            if type(station.town) == str:
                towns.add(station.town)
        return sorted(list(towns))
    towns_name = towns_with_stations(stations)
    townlist = []
    for name in towns_name:
        a, b, tweight = 0, 0, 0
        for station in stations:
            if station.town == name:
                a += station.coord[0]
                b += station.coord[1]
                tweight += 1
        coord = (a/tweight, b/tweight)
        town =  (name, coord)
        townlist.append(town)
    return townlist


def sampling(stations, town):  # town = (name, coord)
    sample_stations = stations_within_radius(stations, town[1], 10)   # sample only stations within 10 km
    return sample_stations

criteria = []

# def critA(station):  #assessing based on current relative level


def sum_criteria(sample_stations, town):
    station_scores = []
    for station in sample_stations:
        for criterion in criteria:
            raw += criterion(station)
        d = haversine(station.coord, town[1])
        station_scores.append((station.name, d, raw))
    return station_scores

def spatial_average (station_scores): #station_scores: list of tuples with (station name, distance from town, station raw score)
    tsum = 0
    tweight = 0
    for i in range(len(station_scores)):
        r = station_scores[i][1]
        raw = station_scores[i][2]
        weight = 1/r  # can edit to 1/r**2 for different weighting
        tsum += raw * weight
        tweight += weight