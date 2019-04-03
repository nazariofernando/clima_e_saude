import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

def checkDays(data, year, days = 365):

    oldShape = data.shape[0]

    if oldShape == days:
        return data

## IDEA: ver se tem mais ou menos do que 365

    meanMax = data.loc[:, data.columns[1]].mean()
    meanMin = data.loc[:, data.columns[2]].mean()

    oldDays = data.index.tolist()

    i = 1

    for j in range(0, oldShape):

        while i != oldDays[j] and i <= days:
            data.loc[i] = [int(year), meanMax, meanMin]
            i += 1
        i += 1

    return data

def checkTemp(data, tempMax, tempMin, year):

    corruptedDataMax1 = data[data[data.columns[1]] > tempMax]
    corruptedDataMax2 = data[data[data.columns[2]] > tempMax]

    corruptedDataMin1 = data[data[data.columns[1]] < tempMin]
    corruptedDataMin2 = data[data[data.columns[2]] < tempMin]

    daysMax1 = corruptedDataMax1.index.tolist()
    daysMax2 = corruptedDataMax2.index.tolist()

    daysMin1 = corruptedDataMin1.index.tolist()
    daysMin2 = corruptedDataMin2.index.tolist()

    newDataMax1 = data.drop(daysMax1)

    meanMax1 = newDataMax1.loc[:, newDataMax1.columns[1]].mean()

    for i in daysMax1:
        newDataMax1.loc[i] = [int(year), meanMax1, data.loc[i].at[data.columns[2]]]

    newDataMax2 = newDataMax1.drop(daysMax2)
    meanMax2 = newDataMax2.loc[:, newDataMax2.columns[2]].mean()

    for i in daysMax2:
        newDataMax2.loc[i] = [int(year), newDataMax1.loc[i].at[data.columns[1]], meanMax2 ]

    newDataMin1 = newDataMax2.drop(daysMin1)
    meanMin1 = newDataMin1.loc[:, newDataMin1.columns[1]].mean()

    for i in daysMin1:
        newDataMin1.loc[i]  = [int(year), meanMin1, newDataMax2.loc[i].at[data.columns[2]]]

    newDataMin2 = newDataMin1.drop(daysMin2)
    meanMin2  = newDataMin2.loc[:, newDataMin2.columns[2]].mean()

    for i in daysMin2:
        newDataMin2.loc[i] =[int(year), newDataMin1.loc[i].at[data.columns[2]], meanMin2 ]


    return newDataMin2



def checkTempMax(data, tempMax, year):


    corruptedData = data[data[data.columns[1]] > tempMax]

    days = corruptedData.index.tolist()

    newData = data.drop(days)

    mean = newData.loc[:, newData.columns[1]].mean()

    for i in days:
        newData.loc[i] = [int(year), mean, corruptedData.loc[i].at[data.columns[2]]]

    return newData

def checkTempMin(data, tempMin, year):


    corruptedData1 = data[data[data.columns[2]] < tempMin]


    days = corruptedData.index.tolist()

    newData = data.drop(days)

    mean = newData.loc[:, data.columns[2]].mean()

    for i in days:
        newData.loc[i] = [int(year), corruptedData.loc[i].at[data.columns[1]], mean]


    return newData

def invertRowsDataFrame(data):

    days = data.index.tolist()
    size = len(days)

    newData = {
        "Dia Juliano": [0] * size,
        "Ano": [year] * size,
        "Temperatura Máxima": [0] * size,
        "Temperatura Mínima": [0] * size
    }

    j = 0
    for i in range(size-1, -1,-1):
        newData["Dia Juliano"][j] = days[i]
        newData["Temperatura Máxima"][j] = data.loc[i].at[data.columns[1]]
        newData["Temperatura Mínima"][j] = data.loc[i].at[data.columns[2]]
        j += 1

    reorganizedData = pd.DataFrame(newData)
    return reorganizedData.set_index(reorganizedData.columns[0])

def invertRowsArray(data):
    size = len(data)
    newData = [[]] * size
    j = 0
    for i in range(size-1, -1, -1):
        newData[j] = data[i]
        j += 1

    return np.array(newData)

def invertColumnsArray(data):
    transposedData = data.T
    return invertRowsArray(transposedData).T

def endOfMonths(diasMes):
    sum = 0
    diasMesAt = [0] * 12
    j = 0

    for m in diasMes:
        diasMesAt[j] = 0
        sum += diasMes[m]
        diasMesAt[j] = sum
        j += 1

    return diasMesAt



def breakInMonths(rawData, diasMes, col, minVal=0):

    days = rawData.index.tolist()

    sum = 0
    diasMesAt = [0] * 12
    j = 0

    for m in diasMes:
        diasMesAt[j] = 0
        sum += diasMes[m]
        diasMesAt[j] = sum
        j += 1


    k = 0
    j = 0
    m = [[]] * 12

    months = list(diasMes.keys())

    d = [0] * diasMes[months[j]]

    for i in range(1, diasMesAt[11]+1):

        if i in days:
            d[k] = rawData.loc[i].at[rawData.columns[col]]

        k += 1

        if i == diasMesAt[j]:
            m[j] = d
            k = 0
            if j != 11:
                j += 1
                d = [0] * diasMes[months[j]]



    for mes in m:
        while 31 - len(mes) > 0:
            mes.append(minVal)

    return np.array(m)
