import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random
import pandas as pd
import csv 

df = pd.read_csv("StudentMarks.csv")
data = df ["Math_score"].tolist()

fig = ff.create_distplot([data], ["Math_Score"],show_hist= False)

fig.show()
