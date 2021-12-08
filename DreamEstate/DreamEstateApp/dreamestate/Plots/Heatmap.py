import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/31-tavg-202111-1.csv')

# Preparing data
data = [go.Heatmap(x=df['Location'],
                   y=df['1901-2000 Mean'],
                   z=df['Value'].values.tolist(),
                   colorscale='Jet')]

# Preparing layout
layout = go.Layout(title='November 2021 NC County Average Temperature', xaxis_title="Location",
                   yaxis_title="1901-2000 Mean")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='../static/heatmap.html')
