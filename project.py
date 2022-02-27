#Example graph
from ctypes.wintypes import PUSHORT
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import numpy as np
import plotly.graph_objects as pgo



#Ran this to see if our packages were working
#print("hi")
data = pd.read_csv('fatal-police-shootings-data.csv')
(data.head())

#Data Cleaning
data.isna().any()

data[["armed", "gender", "race", "flee"]] = data[["armed", "gender", "race", "flee"]].fillna(value="N/A")

(f'Data is {data.duplicated().any()}')

#Helping python understand that date should be recognized in a date format 
data["date"] = data["date"].apply(pd.to_datetime)

#Extracting year from date
data['year'] = pd.DatetimeIndex(data['date']).year


#Extracting month from date 
data['month'] = pd.DatetimeIndex(data['date']).month


#Extract day from date
data['day'] = pd.DatetimeIndex(data['date']).day
print(data.head())

mapping = {}

# for row in csv
for index, row in data.iterrows():
    print(row["state"])
    break 

#Choropleth map 
fig = pgo.Figure(graph1=pgo.Choropleth(
    locations=data['state'], # Spatial coordinates
    z = data[''].astype(float), # Data to be color-coded
    locationmode = 'USA-states', # set of locations match entries in `locations`
    colorscale = 'Reds',
    colorbar_title = "Millions USD",
))

fig.update_layout(
    title_text = '2011 US Agriculture Exports by State',
    geo_scope='usa', # limite map scope to USA
)

fig.show()




#PieCharts 
armed = data["armed"].value_counts()

arm = px.pie(armed, values=armed.values, names=["gun", "knife", "unarmed"], title="Top Three Weapons", color_discrete_sequence=["blue", "orange", "yellow"], hole=0.4)
arm.update_layout(font_size=16)
arm.update_traces(textfont_size=18, textposition="inside",hoverinfo='label+percent')
arm.show()

git commit -a -am “adding project”
git PUSHORT