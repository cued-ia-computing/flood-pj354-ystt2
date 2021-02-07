from floodsystem.stationdata import build_station_list, update_water_levels


def stations_over_threshold(stations, tol):
    update_water_levels(stations)
    riskstations = []
    for station in stations:
        relative = station.relative_water_level()
        if type(relative) == float:
            if relative >= tol:
                riskstations.append((station.name, relative))
    return riskstations

def stations_highest_rel_level(stations, N):
    risklist = stations_over_threshold(stations, 0)
    risklist.sort(key=lambda x:x[1])
    return risklist[-(N+1):-1]