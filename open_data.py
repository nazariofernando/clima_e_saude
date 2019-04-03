import pandas as pd

def openFile(filePath, ano, sheet):
    file = pd.read_excel(filePath, sheet_name =sheet, usecols=[1, 2, 12, 14])
    return file[file[file.columns[0]]==int(ano)]
