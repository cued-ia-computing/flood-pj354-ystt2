# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

#just need to fix the importing issues

from .stationdata import build_station_list
from .utils import sorted_by_key  # noqa
from haversine import haversine, Unit

def stations_by_distance(stations, p):
    pairlist = []
    for station in stations:
        d = haversine(station.coord, p)
        coordpair = (station.name, d)
        pairlist.append(coordpair)
    return sorted(pairlist, key=lambda station: station[1])

def stations_with_radius(stations, centre, r):
    pairlist = stations_by_distance(stations, centre)
    i = 0
    stationlist = []
    while True:
        if pairlist[i][1] < r:
            stationlist.append(pairlist[i][0])
            i += 1
        else:
            return stationlist
            
