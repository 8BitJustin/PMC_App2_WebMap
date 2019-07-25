import folium
import pandas

# Opens and reads volcanoes.txt file
data = pandas.read_csv("Volcanoes.txt")
# These variables create lists from these specific columns within the txt file
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
elev = list(data["ELEV"])


# Provides color to volcano marker (used below) depending on the elevation (from the elev list)
def color_prod(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation < 3000:
        return 'orange'
    else:
        return 'red'


# This creates the actual map with specific location centered, zoom level, and type of tile setup
map = folium.Map(location=[41.988748, -112.635234], zoom_start=5, tiles="Stamen Terrain")

# Feature group for volcanoes, helps with layers
fgv = folium.FeatureGroup(name="Volcanoes")

# For loop. Runs through all four variable lists above using zip, creates circle marker at lat/lon, provides name and
# uses the color_prod() function, to point out all volcanoes (used with fgv feature group above)
for lt, ln, nm, el in zip(lat, lon, name, elev):
    fgv.add_child(folium.CircleMarker(location=[lt,ln],
                                      radius=6,
                                      popup=nm + " " + str(el),
                                      fill_color=color_prod(el),
                                      color='grey',
                                      fill_opacity=0.7))

# Another feature group for population
fgp = folium.FeatureGroup(name="Population")

# Still trying to understand this, lolz. Ok, population group opens the world.json file and reads. Uses similar
# technique as the lists, pulling data based on properties. Uses those to decipher which color to use for each
# country based on population.
fgp.add_child(folium.GeoJson(data=open("world.json", "r", encoding="utf-8-sig").read(), style_function=lambda x: {
    "fillColor": "green" if x["properties"]['POP2005'] < 10000000 else "orange" if 10000000 <= x["properties"][
        "POP2005"] < 20000000 else "red"}))

# Adds both groups to map
map.add_child(fgv)
map.add_child(fgp)

# Adds control layer
map.add_child(folium.LayerControl())

# Saves all info here to html in file
map.save("map_1.html")