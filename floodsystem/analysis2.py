import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from haversine import haversine, Unit
from floodsystem.geo import stations_by_distance, stations_within_radius, stations_by_river
from . import datafetcher
from floodsystem.stationdata import build_station_list, update_water_levels
from floodsystem.analysis import polyfit, get_poly



def ddx(y, x): #where y is the function you want to differentiate. Y must be a np.polynomial TYPE!!! 
#where x is the point at where you want the value of the gradient to be!
    D = np.polyder(y)
    value = np.polyval(D, x)
    return value

def d2dx2(y,x):
    D = np.polyder(y)
    D2 = np.polyder(D)
    value = np.polyval(D2, x)
    return value

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


def critA(station):  #assessing based on first derivative
    try:
        get_poly(station)
        pass
    except TypeError:
        return 0
    y = get_poly(station)[1]
    x = get_poly(station)[0]
    D = ddx(y, x)
    if D > 0:
        return 1
    else:
        return 0

def critB(station):  #assessing based on second derivative
    try:
        get_poly(station)
        pass
    except TypeError:
        return 0
    y = get_poly(station)[1]
    x = get_poly(station)[0]
    D2 = d2dx2(y, x)
    if D2 > 0:
        return 1
    else:
        return 0

def critC(station):   #based on current relative level
    rel = station.relative_water_level()
    if type(rel) == float:
        if rel > 2:
            return 4
        elif rel <0:
            return 0
        else:
            return 2*rel

def critD(station):   #based on other stations along the same river
    stations = build_station_list()
    update_water_levels(stations)
    river = station.river
    stations_along = stations_by_river(stations)[river]
    relatives = []
    for sta_name in stations_along:
        for s2 in stations:
            if s2.name == sta_name:
                rel = s2.relative_water_level()
                if type(rel) == float:
                    relatives.append(rel)
    river_mean = np.mean(relatives)
    if river_mean > 2:
        return 2
    elif river_mean <0:
        return 0
    else:
        return river_mean  #directly return the mean rel level of the river

criteria = [critA, critB, critC, critD]

def sum_criteria(sample_stations, town, stations):
    station_scores = []
    for sta_name in sample_stations:
        for s2 in stations:
            if s2.name == sta_name:
                raw = 0
                for criterion in criteria:
                    raw += criterion(s2)
                    d = haversine(s2.coord, town[1])
                station_scores.append((s2.name, d, raw))
    return station_scores

def spatial_average (station_scores): #station_scores: list of tuples with (station name, distance from town, station raw score)
    tsum = 0
    tweight = 0
    for i in range(len(station_scores)):
        r = station_scores[i][1]
        raw = station_scores[i][2]
        weight = 1/(r**0.2+0.1)  # can edit to 1/r**n for different weighting
        tsum += raw * weight
        tweight += weight
    return(tsum/tweight)


def rate(spat):
    if spat > 3:
        return "severe"
    elif spat > 2:
        return "high"
    elif spat > 1:
        return "moderate"
    else:
        return "low"