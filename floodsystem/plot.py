from . import analysis

def plot_water_level_with_fit(station, dates, levels, p):
    analysis.polyplot(station