from floodsystem import analysis
from floodsystem import station
from floodsystem import stationdata
from floodsystem import datafetcher

stations = stationdata.build_station_list()
station_1 = stations[1]
print(station_1)
id = station_1.measure_id
dates, levels = datafetcher.fetch_measure_levels(id,48)
#converting datetime into float
dates_float = matplotlib.dates.date2num(dates)
#plotting the thing now


poly(dates_float, levels, 3)