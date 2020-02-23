import pandas as pd
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import pandas as pd
from geopy import distance
import csv



allio = ('dict.csv')
df = pd.read_csv(allio)
fig = go.Figure(go.Densitymapbox(lat=df.latitude_all, lon=df.longitude_all, z=df.signal_all, radius=10))
fig.update_layout(mapbox_style="stamen-terrain", mapbox_center_lon=180)
fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0})
# fig.show()





points=[]
with open (allio, 'r') as file:
    reader = csv.DictReader(file)
    
    for row in reader:
    
        point = [row['latitude_all'], row['longitude_all']]

        points.append(point)
q =len(points)

a = 0
dists=[]
while a < q:
    point1 = points[a]
    # print(point1)
    
    a = a + 1
    point2 =points[a]
    # print(point1)
    a = a + 1


    dist = distance.distance(point1, point2).km
    dists.append(dist)
    if a == q:
        print(a)
        break
def distssum(dists):
    a = 0
    for i in dists:
        a = a + i
    return a

dis1 = distssum(dists)
dis1 = round(dis1, 3)
dis1 = (dis1, "пройдено километров")
dis1 = str(dis1)


dis2 = dis1
# dis2 = (distssum(dists), 'km'.encode())


fig = go.Figure()

fig.add_trace(
    go.Scatter(
        x=df["num_point"],
        y=df["signal_all"],
        mode="lines",
        name="signal"
    )    
)
fig.update_layout(
    height=800,
    showlegend=False,
    title_text= (dis2) ,
)

fig.show()