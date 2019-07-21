import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])

map = folium.Map(location=[32.295760, -110.979765], zoom_start=11,
                 tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt,ln],
                               popup="Hi, I'm a marker!",
                               icon=folium.Icon(color="blue")))

map.add_child(fg)

map.save("map_1.html")