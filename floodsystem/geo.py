# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

#just need to fix the importing issues

from .stationdata import build_station_list
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


def generate_rivers(stations):
    Rivers_StationNumber = []
    for i in stations:
        Rivers_StationNumber[i.river] = (i.station_id)
    return Rivers_StationNumber

def finding_in_river_list(river_name, Rivers_D): #adding number, Rivers_D is a nested list of the triples.
    new = []
    for list in Rivers_D: #List is sub list within Rivers_D, that should contain name, station, number
        for i in list:
            if i == river_name:
                list[2] = list[2] + 1
                print(list[2])
    for list in Rivers_D:
        if list[2] > 1:
            new.append(list[2])
    return new

    


def rivers_by_station_number(stations, N):
    Rivers_D = [] 
    Rivers_StationNumber = generate_rivers(stations)
    for i in Rivers_StationNumber.items(): 
        if i in Rivers_StationNumber
        for j in i:
            temp.append(j)
        temp.append(0)
        Rivers_D.append(temp)
        print(i[0])
        if i[0] in Rivers_D:
            print("hi")
            river_name = i[0]
            finding_in_river_list(river_name, Rivers_D)
            
        



    
    