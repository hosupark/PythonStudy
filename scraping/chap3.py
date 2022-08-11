import os
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rc

# print(os.getcwd())

df = pd.read_csv("./PythonWorkspace/scraping/TestData/stationlist_enum_test.csv")

# print(df)
print(len(df))
# print(df.columns.values)
# print(df.index.values)
# print(df[["#노선명","정류소명"]]) 
print(df.drop(28, axis=0))
# print(len(df))
# print(df[df["순번"]>10])
print(df["X좌표"].min())
print(df["X좌표"].max())

rc('font', family='AppleGothic')
plt.rcParams['axes.unicode_minus']=False
temp = df['X좌표']
print(temp)
# temp.plot.bar()
# df.plot()
# plt.show()
temp.plot()
plt.savefig("figure.png")
