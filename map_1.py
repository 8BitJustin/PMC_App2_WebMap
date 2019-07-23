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


map = folium.Map(location=[41.988748, -112.635234], zoom_start=5, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")

for lt, ln, nm, el in zip(lat, lon, name, elev):
    fg.add_child(folium.CircleMarker(location=[lt,ln],
                                     radius=6,
                                     popup=nm + " " + str(el),
                                     fill_color=color_prod(el),
                                     color='grey',
                                     fill_opacity=0.7))

fg.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(), style_function=lambda x: {
    "fillColor": "green" if x["properties"]['POP2005'] < 10000000 else "orange" if 10000000 <= x["properties"][
        "POP2005"] < 20000000 else "red"}))

map.add_child(fg)

map.save("map_1.html")