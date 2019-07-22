import folium
import pandas

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])

def color_prod(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[41.988748, -112.635234], zoom_start=5,
                 tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, nm, el in zip(lat, lon, name, elev):
    fg.add_child(folium.Marker(location=[lt,ln],
                               popup=nm + " " + str(el),
                               icon=folium.Icon(color=color_prod(el))))

map.add_child(fg)

map.save("map_1.html")