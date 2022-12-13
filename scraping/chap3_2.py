import os
import pandas as pd
import openpyxl

os.chdir("./PythonWorkspace/scraping/")

df = pd.read_excel("./TestData/csv_to_excel_3.xlsx")
print(df)
df = pd.read_excel("./TestData/csv_to_excel_3.xlsx", sheet_name='국어정렬')
print(df)