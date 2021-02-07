# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module provides a model for a monitoring station, and tools
for manipulating/modifying station data

"""

class MonitoringStation:
    """This class represents a river level monitoring station"""

    def __init__(self, station_id, measure_id, label, coord, typical_range,
                 river, town):

        self.station_id = station_id
        self.measure_id = measure_id

        # Handle case of erroneous data where data system returns
        # '[label, label]' rather than 'label'
        self.name = label
        if isinstance(label, list):
            self.name = label[0]

        self.coord = coord
        self.typical_range = typical_range #YES T MONEY THERE IS
        self.river = river
        self.town = town

        self.latest_level = None #YES WHAT IS THIS T MONEY??? WHAT DOES IT FETCH?

    def __repr__(self):
        d = "Station name:     {}\n".format(self.name)
        d += "   id:            {}\n".format(self.station_id)
        d += "   measure id:    {}\n".format(self.measure_id)
        d += "   coordinate:    {}\n".format(self.coord)
        d += "   town:          {}\n".format(self.town)
        d += "   river:         {}\n".format(self.river)
        d += "   typical range: {}".format(self.typical_range)
        return d

    def typical_range_consistent(self):
        if self.typical_range == None:
            return False
        elif self.typical_range[0] > self.typical_range[1]:
            return False
        else:
            True


    def inconsistent_typical_range_stations(self): #Checking the range, task 1F
        if self.typical_range == None:
            return False
        else:
            if self.typical_range[0] > self.typical_range[1]:
                return False
    
    def relative_water_level(self):
        if self.latest_level != None and self.typical_range != None:
            if self.typical_range[0] < self.typical_range[1]:
                lowbound = self.typical_range[0]
                upbound = self.typical_range[1]
                relative = (self.latest_level-lowbound)/(upbound-lowbound)
                return relative
    