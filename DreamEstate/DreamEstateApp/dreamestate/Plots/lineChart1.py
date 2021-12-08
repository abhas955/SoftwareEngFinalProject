import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/homeValueEstimation.csv')

# Filtering US Cases
filtered_df = df[df['StateName'] == 'NC']


# Preparing data
data = [go.Scatter(x=df['CountyName'], y=df['ForecastYoYPctChange'], mode='lines', name='Home Value Estimate')]

# Preparing layout
layout = go.Layout(title='Home Value Estimate for 2022', xaxis_title="CountyName",
                   yaxis_title="Forecast Percentage Change in Price")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='../static/linechart1.html')


