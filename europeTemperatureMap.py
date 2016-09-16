import plotly.plotly as py
import pandas as pd
import pyowm
import json
import time
from optparse import OptionParser
from geopy.geocoders import Nominatim

parser = OptionParser()
parser.add_option("-a", "--api", dest="api",help="api key to get access to openweather")

(opts, args) = parser.parse_args()
api=opts.api

geolocator = Nominatim()

owm = pyowm.OWM(api)
df = pd.read_csv('cities.csv')
df.head()

for index, row in df.iterrows():
  loc_city = df.loc[index,"city"] + "," + df.loc[index,"country"]

  iterate = True
  counter = 0
  while (iterate and counter < 5):
      try:
          location = geolocator.geocode(df.loc[index,"city"])
          observation = owm.weather_at_coords(location.latitude,location.longitude)
          w = observation.get_weather()
          jsonweather = w.to_JSON()
          jsonloads = json.loads(jsonweather)
          df.loc[index, "temp"] = jsonloads["temperature"]["temp"] - 273.15
          df.loc[index, "long"] = location.longitude
          df.loc[index, "lat"] = location.latitude
          df.loc[index, "text"] = loc_city + ' Temperature ' + str(df.loc[index, "temp"])
          iterate = False
      except:
          iterate = True
          counter = counter + 1


scl = [ [0,"rgb(5, 10, 172)"],[0.35,"rgb(40, 60, 190)"],[0.5,"rgb(70, 100, 245)"],\
    [0.6,"rgb(90, 120, 245)"],[0.7,"rgb(106, 137, 247)"],[1,"rgb(220, 220, 220)"] ]


data = [ dict(
        type = 'scattergeo',
        #locationmode = 'contry names',
        lon = df['long'],
        #lon = location.longitude,
        lat = df['lat'],
        #lat = location.latitude,
        text = df['text'],
        #text = 'Lodon,uk',
        mode = 'markers',
        marker = dict(
            size = 8,
            opacity = 0.8,
            reversescale = True,
            autocolorscale = False,
            symbol = 'square',
            line = dict(
                width=1,
                color='rgba(102, 102, 102)'
            ),
            colorscale = scl,
            cmin = df['temp'].min(),
            color = df['temp'],
            cmax = df['temp'].max(),
            #cmax = 50,
            colorbar=dict(
                title="Temperature Scale"
            )
        ))]

layout = dict(
        title = 'Temperature Map<br>(Hover for city names and temperatures)',
        colorbar = True,
        geo = dict(
            scope='europe',
            projection=dict( type='natural earth' ),
            showland = True,
            landcolor = "rgb(250, 250, 250)",
            subunitcolor = "rgb(217, 217, 217)",
            countrycolor = "rgb(217, 217, 217)",
            countrywidth = 0.5,
            subunitwidth = 0.5
        ),
    )

fig = dict( data=data, layout=layout )
py.plot( fig, validate=False, filename='d3-europeTemperatureMap' )
