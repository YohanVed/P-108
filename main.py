import plotly.figure_factory as ff
import pandas as pd
import csv

df = pd.read_csv("studentdata.csv")

fig  =  ff.create_distplot([df["Days Present"].tolist()], ["Days Present"])
fig .show()