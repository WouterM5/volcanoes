import folium
import pandas

#data = pandas.read_csv("Volcanoes.txt")
data = pandas.read_csv("volcanoes.txt",sep=";",encoding = "ISO-8859-1")

lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return "green"
    elif elevation < 2000:
        return "purple"
    elif elevation < 3000:
        return "orange"
    elif elevation < 4000:
        return "blue"
    else:
        return "red"

map = folium.Map(location=[38.58, -99.09], zoom_start=4, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="Volcanoes")

for lt, ln, el in zip(lat, lon, elev):
    fg.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+" m", fill_color = color_producer(el), color ="grey", fill_opacity=0.8))

fg2 = folium.FeatureGroup(name="Population")
fg2.add_child(folium.GeoJson(data = open("world.json", "r", encoding="utf-8-sig").read(),style_function=lambda x: {"fillColor":"green" if x["properties"]["POP2005"] < 10000000 else "orange" if 10000000 <= x["properties"]["POP2005"] < 20000000 else "red"}))



map.add_child(fg2)
map.add_child(fg)
map.add_child(folium.LayerControl())
map = map.save("Map1.html")

