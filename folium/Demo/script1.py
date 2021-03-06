# how to add points to map
import folium
import pandas

df=pandas.read_csv("Volcanoes_USA.txt")

map=folium.Map(location =[45.372,-121.697], zoom_start=4, tiles='Stamen Terrain')

def color(elev):
    if elev in range(0,1000):
        col='green'
    elif elev in range(1000,3000):
        col='orange'
    else:
        col='red'
    return col

for lat,lon,name,elev in zip(df['LAT'],df['LON'],df['NAME'],df['ELEV']):
    map.simple_marker(location=[lat,lon], popup=name, marker_color="green" \
        if elev in range(0,1000) else "orange" if elev in range(1000,3000) else "red")

# map.simple_marker(location=[45.3311,-121.7731],popup='Timberlake Lodge',marker_color='green')4v
# map.save(path='test2.html')
map.create_map(path='test3.html')





