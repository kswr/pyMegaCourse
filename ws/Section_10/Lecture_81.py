import folium, pandas

data = pandas.read_csv("../input/Lecture_78_data/Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[52.250265,21.017909], zoom_start=8, tiles="openstreetmap")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+ " m", fill_color=color_producer(el), color = 'grey', fill_opacity=0.7))

map.add_child(fg)
map.save("../output/Lecture_81_map.html")