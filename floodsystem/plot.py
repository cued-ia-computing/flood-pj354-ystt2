from .analysis import poly
import matplotlib
import matplotlib.pylab as plt
import numpy as np

def plot_water_level_with_fit(dates, levels, p):
    plt.plot(dates, poly(levels))