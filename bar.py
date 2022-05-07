import plotly.express as px
import csv
import pandas as pd

df = pd.read_csv("data.csv")

fig = px.bar(df, x ="Mobile Brand", y ="Avg Rating")
fig.show()
