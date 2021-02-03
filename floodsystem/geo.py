# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

#just need to fix the importing issues
from collections import Counter
from .stationdata import build_station_list
import operator
from .utils import sorted_by_key  # noqa
#from haversine import haversine, Unit

#def stations_by_distance(stations, p):
 #   pairlist = []
  #  for station in stations:
   #     d = haversine(station.coord, p)
    #    coordpair = (station.name, d)
     #   pairlist.append(coordpair)
    #return sorted(pairlist, key=lambda station: station[1])

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
            
def rivers_with_stations(stations):
    rivers = set([])
    for station in stations:
        rivers.add(station.river)
    return rivers

def stations_by_river(stations):
    out = {}
    for station in stations:
        river = station.river
        if river in out:
            out[river].append(station.name)
        else:
            out[river] = [station.name]
    return out


def generate_rivers(stations): #Generate list of list of rivers, 
    Rivers_StationNumber = []
    for i in stations:
        Rivers_StationNumber.append(i.river) 
    return Rivers_StationNumber

def reverse_dictionary(d): #guess what this does
    sorted_d = dict(sorted(d.items(), key=operator.itemgetter(1),reverse=True))
    return sorted_d


def rivers_by_station_number(stations, N):
    Rivers_StationNumber = generate_rivers(stations) #List of Rivers
    RiverCount = Counter(Rivers_StationNumber) #Dictionary
    Goodboy = reverse_dictionary(RiverCount) # Reverse dictionary to have descending value.
    counter = 0
    FinalList = []
  #  Goodboy = dict(sorted(RiverCount.items(), key=lambda item: item[1]))
    for items in Goodboy.items():
        counter = counter + 1
        FinalList.append(items)
        if counter > N-1:
            break
    return FinalList


        


            
        



    
    