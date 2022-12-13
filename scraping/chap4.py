import os
import pandas as pd

# print(os.getcwd())

os.chdir("./scraping/")
# print(os.getcwd())
df = pd.read_csv("./TestData/20200602_SEOUL.csv", header=None)
# print(len(df))
# print(df.columns.values)

# result = df[df[0]==2561]
# print(result[[0, 1, 2, 3, 4]])

result = df[df[3] == "개포로"]
print(result)

result = df[df[3].str.contains("개포로")]
print(result)
