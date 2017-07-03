import folium
import pandas

data = pandas.read_csv("../input/Lecture_78_data/Volcanoes.txt")

lat = list(data["LAT"])
lon = list(data["LON"])

map = folium.Map(location=[52.250265,21.017909], zoom_start=8, tiles="openstreetmap")

fg = folium.FeatureGroup(name="My Map")

for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup="Hi I am a Marker", icon=folium.Icon(color='green')))

map.add_child(fg)

folium.LayerControl().add_to(map)

map.save("../output/Lecture_78_map.html")
