import folium
import pandas

data = pandas.read_csv("../input/Lecture_78_data/Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

map = folium.Map(location=[52.250265,21.017909], zoom_start=8, tiles="openstreetmap")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.Marker(location=[lt, ln], popup=str(el)+ " m", icon=folium.Icon(color='green')))

map.add_child(fg)

folium.LayerControl().add_to(map)

map.save("../output/Lecture_79_map.html")
