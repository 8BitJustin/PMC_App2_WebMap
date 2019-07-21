import folium

map = folium.Map(location=[32.295760, -110.979765], zoom_start=11,
                 tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for coordinates in [[32.338879, -110.976696], [32.226277, -111.001049]]:
    fg.add_child(folium.Marker(location=coordinates,
                               popup="Hi, I'm a marker!",
                               icon=folium.Icon(color="blue")))

map.add_child(fg)

map.save("map_1.html")