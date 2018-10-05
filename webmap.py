import folium
import pandas as pd
#print dir(folium) shows the modules attributes
map = folium.Map(location=[45.873640, 22.909920], zoom_start=10) #tiles = "Stamen Terrain" changes the fillter of the map

df = pd.read_csv('Volcanoes.txt')

folium.Marker(location=[45.873640, 22.909920], popup="here", icon=folium.Icon(icon="cloud")).add_to(map)
folium.Marker(location=[45.867916, 22.911163], popup="here", icon=folium.Icon(color="red")).add_to(map)

def color(elev):
    if elev in range(0, 999):
        col = "green"
    elif elev in range(1000,1999):
        col = "orange"
    elif elev in range(1999,2999):
        col = "red"
    else:
        col = "gray"
    return col

for lat, lon, name, elev in zip(df["LON"], df["LAT"], df["NAME"], df["ELEV"]):
    folium.Marker(location=[lon, lat], popup=folium.Popup(name + " Heigth: " + str(elev)), icon=folium.Icon(color=color(elev), icon="cloud")).add_to(map)



print map.save("test.html")

