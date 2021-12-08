import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/violentCrimes.csv')


# Preparing data
data = [go.Scatter(x=df['State'], y=df['totalCases'], mode='lines', name='Violent Crimes')]

# Preparing layout
layout = go.Layout(title='Violent Crimes From 1990 to 2019', xaxis_title="State",
                   yaxis_title="Total Cases of Violent Crimes")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='../static/linechart.html')
