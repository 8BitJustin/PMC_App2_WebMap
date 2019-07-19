import folium

map = folium.Map(location=[32.338879, -110.976696], zoom_start=10, tiles="Stamen Terrain")

map.save("map_1.html")