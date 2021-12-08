import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

# Load CSV file from Datasets folder
df = pd.read_csv('../Datasets/homeValueEstimation.csv')

# Filtering US Cases
filtered_df = df[df['StateName'] == 'NC']

# Removing empty spaces from State column to avoid errors
filtered_df = filtered_df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)

# Creating sum of number of cases group by State Column
new_df = filtered_df.groupby(['CountyName'])['ForecastYoYPctChange'].sum().reset_index()

# Sorting values and select first 20 states
new_df = new_df.sort_values(by=['ForecastYoYPctChange'], ascending=[False]).head(20)

# Preparing data
data = [go.Bar(x=new_df['CountyName'], y=new_df['ForecastYoYPctChange'])]

# Preparing layout
layout = go.Layout(title='Forecast of Percentage Change of Home Prices in NC Counties from October 2021 to October 2022', xaxis_title="Counties in NC",
                   yaxis_title="Forecast of Percentage Change")

# Plot the figure and saving in a html file
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='../static/barchartHomeEstimation.html')
