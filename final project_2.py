import pandas as pd
import folium
from IPython.display import display


df_mine= pd.read_csv('Police_Department_Incidents_-_Previous_Year__2016_.csv')
print(df_mine)

#df_can.drop(['AREA','REG','DEV','Type','Coverage'], axis=1, inplace=True)
df_new = df_mine.groupby('PdDistrict').count()
df_new = df_new.reset_index('PdDistrict')
df_new = df_new[['PdDistrict','Category']]
df_new.rename(columns={'PdDistrict':'Neighborhood', 'Category':'Count'}, inplace=True)
print(df_new)

world_geo = r'san-francisco.geojson' # geojson file

world_map = folium.Map(location=[37.77, -122.42], zoom_start=12, tiles='Mapbox Bright')
folium.Choropleth(
    geo_data=world_geo,
    data=df_new,
    columns=['Neighborhood', 'Count'],
    key_on='feature.properties.DISTRICT',
    fill_color='YlOrRd', 
    fill_opacity=0.7, 
    line_opacity=0.2,
    legend_name='Crime Rate in San Francisco'
).add_to(world_map)

display(world_map)
#, tiles='Mapbox Bright'
#world_map.save(outfile='testScores.html')