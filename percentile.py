import pandas as pd
import numpy as np
from open_data import openFile
import organize_data as od


def calcHW(data, col):

    percent = np.percentile(data[col], 90)

    print(percent)

    return data[data[col] >= percent]

def findHWs(data, year):

    days = data.index.tolist()

    tempHWDay = []
    tempHWYear = []
    tempHWTM = []
    tempHWTm = []

    newData = {
        "Dia Juliano": [],
        "Ano": [],
        "Temperatura Máxima": [],
        "Temperatura Mínima": []
    }

    k = 0
    j = 0
    i = 0

    size = len(days)

    while j < size:
        i = days[j]
        while j < size and i == days[j]:
            tempHWDay.append(days[j])
            tempHWYear.append(year)
            tempHWTM.append(data.loc[i].at[data.columns[1]])
            tempHWTm.append(data.loc[i].at[data.columns[2]])
            k += 1
            j += 1
            i += 1

        if k >= 3:
            newData["Dia Juliano"] += tempHWDay
            newData["Ano"] += tempHWYear
            newData["Temperatura Máxima"] += tempHWTM
            newData["Temperatura Mínima"] += tempHWTm

        tempHWDay = []
        tempHWYear = []
        tempHWTM = []
        tempHWTm = []
        k = 0

    HW1 = pd.DataFrame(newData)

    HW2 = HW1.set_index(HW1.columns[0])

    return HW2
