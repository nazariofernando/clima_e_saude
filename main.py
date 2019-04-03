from open_data import openFile
import percentile as pc
import organize_data as od
import graphics as gp

year1999 = {
    "Janeiro": 31,
    "Fevereiro": 28,
    "Março": 31,
    "Abril": 30,
    "Maio": 31,
    "Junho": 30,
    "Julho": 31,
    "Agosto": 31,
    "Setembro": 30,
    "Outubro": 31,
    "Novembro": 30,
    "Dezembro": 31
}

year2009 = {
    "Janeiro": 31,
    "Fevereiro": 28,
    "Março": 31,
    "Abril": 30,
    "Maio": 31,
    "Junho": 30,
    "Julho": 31,
    "Agosto": 31,
    "Setembro": 30,
    "Outubro": 31,
    "Novembro": 30,
    "Dezembro": 31
}

year2018 = {
    "Janeiro": 31,
    "Fevereiro": 28,
    "Março": 31,
    "Abril": 30,
    "Maio": 31,
    "Junho": 30,
    "Julho": 31,
    "Agosto": 31,
    "Setembro": 30,
    "Outubro": 31,
    "Novembro": 30,
    "Dezembro": 31
}

years = { "1999": year1999, "2009": year2009, "2018": year2018 }


year = input("Coloque o ano que vamos estudar: ")
code = input("Coloque qual é o código do banco de dados que vamos usar: ")

rawData = openFile("./dados/" + year + ".xlsx", year, code)

endOfMonths = od.endOfMonths(years[year])

indexedData = rawData.set_index(rawData.columns[1])

correctedTemps = od.checkTemp(indexedData, 44.80, 3.89, year)

tempMax = pc.calcHW(correctedTemps, indexedData.columns[1])
tempMin = pc.calcHW(correctedTemps, indexedData.columns[2])



HWTempMax = pc.findHWs(tempMax, year)
HWTempMin = pc.findHWs(tempMin, year)

calendarTempMax = od.breakInMonths(HWTempMax, years[year], 2)
calendarTempMin = od.breakInMonths(HWTempMin, years[year], 2)

gp.graphCalendar(calendarTempMax, year, correctedTemps.columns[1])
gp.graphCalendar(calendarTempMin, year, correctedTemps.columns[2])

fixedData = od.checkDays(correctedTemps, year)

#gp.yearHistogram(fixedData)

gp.scatterPlot(fixedData, HWTempMax, fixedData.columns[1], year)
gp.scatterPlot(fixedData, HWTempMin, fixedData.columns[2], year)

gp.lines(fixedData, HWTempMax, fixedData.columns[1], endOfMonths, year)
gp.lines(fixedData, HWTempMin, fixedData.columns[2], endOfMonths, year)
