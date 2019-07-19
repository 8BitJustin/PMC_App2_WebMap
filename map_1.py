import folium

map = folium.Map(location=[32.338879, -110.976696], zoom_start=10,
                 tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[32.338879, -110.976696],
                            popup="Hi, I'm a marker!",
                            icon=folium.Icon(color="green")))
map.add_child(fg)

map.save("map_1.html")