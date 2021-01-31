from floodsystem.stationdata import build_station_list

stations = build_station_list()
for station in stations:
        if station.name in ['Oakington']:
            print(station.river)

