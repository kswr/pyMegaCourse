import folium

map = folium.Map(location=[52.250265,21.017909], zoom_start=12, tiles="openstreetmap")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[52.250265,21.017909], popup="Hi I am a Marker", icon=folium.Icon(color='green')))
map.add_child(fg)

# folium.TileLayer('stamentoner').add_to(map)
# folium.TileLayer('stamenterrain').add_to(map)
# folium.TileLayer('stamenwatercolor').add_to(map)
# folium.TileLayer('mapquestopen').add_to(map)
# folium.TileLayer('MapQuest Open Aerial').add_to(map)
# folium.TileLayer('Mapbox Bright').add_to(map)
# folium.TileLayer('Mapbox Control Room').add_to(map)
# folium.TileLayer('cartodbpositron').add_to(map)
# folium.TileLayer('cartodbdark_matter').add_to(map)

folium.LayerControl().add_to(map)

map.save("../output/Lecture_76_map.html")
