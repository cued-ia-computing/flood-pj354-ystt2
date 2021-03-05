from .stationdata import build_station_list, update_water_levels


def stations_level_over_threshold(stations, tol):
    update_water_levels(stations)
    riskstations = []
    for station in stations:
        relative = station.relative_water_level()
        if type(relative) == float:
            if relative >= tol:
                riskstations.append((station.name, relative))
    riskstations = sorted(riskstations, key=lambda x: x[1], reverse = True)
    return riskstations

def stations_highest_rel_level(stations, N):
    risklist = stations_level_over_threshold(stations, 0)
    ranklist = []
    for i in range(0,N):
        for station in stations:
            if station.name == risklist[i][0]:
                ranklist.append(station)
    return ranklist