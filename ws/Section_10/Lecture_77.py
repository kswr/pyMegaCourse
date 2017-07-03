import folium

map = folium.Map(location=[52.250265,21.017909], zoom_start=8, tiles="openstreetmap")

fg = folium.FeatureGroup(name="My Map")

for coordinates in [[52.250265,21.017909],[52.550265,21.117909]]:
    fg.add_child(folium.Marker(location=coordinates, popup="Hi I am a Marker", icon=folium.Icon(color='green')))

map.add_child(fg)

folium.LayerControl().add_to(map)

map.save("../output/Lecture_77_map.html")
