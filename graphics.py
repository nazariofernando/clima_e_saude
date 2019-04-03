import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import heatmap as hm
import organize_data as od
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

def lines(data, hw, col, daysMonth, year):

    size = data.shape[0]

    t = data.index.tolist()
    s = data[col]

    fig, (vax) = plt.subplots(1, figsize=(12, 6))

    days = hw.index.tolist()

    colors = ['blue'] * size


    for i in days:
        colors[i-1] = 'red'

    min = data[col].min()
    max = data[col].max()

    vax.vlines(t, [min-5], s, colors=colors)
    # By using ``transform=vax.get_xaxis_transform()`` the y coordinates are scaled
    # such that 0 maps to the bottom of the axes and 1 to the top.
    vax.vlines(daysMonth, min-5, max+5, colors='black')
    vax.set_xlabel('Dias Julianos')
    vax.set_ylabel('Temperatura em Celsius')
    vax.set_title('Temperaturas e ondas de calor a partir da ' + col +  ' em ' + str(year))

    plt.show()


def scatterPlot(data, hw, col, year):

    size = data.shape[0]

    days = hw.index.tolist()

    x = range(1, size+1)
    y = data[col]

    fig, ax = plt.subplots()

    ax.set_xlabel('Dias Julianos')
    ax.set_ylabel('Temperatura em Celsius', fontsize=15)
    ax.set_title('Distribuição de ondas de calor a partir das ' + str(col) + ' no ano de ' + str(year))

    colors = ['blue'] * size

    for i in days:
        colors[i-1] = 'red'


    ax.scatter(x, y, c=colors, alpha=0.5)
    fig.tight_layout()
    plt.show()


def yearHistogram(data):

    size = data.shape[0]

    # Generate a normal distribution, center at x=0 and y=5
    x = data[data.columns[1]].values

    y = data[data.columns[2]].values

    fig, axs = plt.subplots(1, 2)

    # We can set the number of bins with the `bins` kwarg
    axs[0].hist(x, bins=size)
    axs[1].hist(y, bins=size)


    fig.tight_layout()
    plt.show()



def graphCalendar(data, year, col, inverse = True, transposed=True):

    months = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
              "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]

    if transposed:
        data = data.T

    if inverse:
        days = range(31, 0, -1)
        data = od.invertRowsArray(data)
        #data = od.invertColumnsArray(data)
    else:
        days = range(1, 32)


    fig, ax = plt.subplots()

    im = hm.heatmap(data, days, months, ax=ax,
                       cmap="Wistia", aspect="auto")
    #texts = hm.annotate_heatmap(im, valfmt="{x:.1f} t")'

    ax.set_title("Distribuição de Ondas de Calor a partir das " + col + " no Ano de " + str(year))

    fig.tight_layout()
    plt.show()
