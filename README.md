# python_weather_plotly
This is an example of python program that reads a list of european cities from a csv file and it plots temperature data in a map

The project is composed with 2 files

1. europeanTemperatureMap.py: Python script to get weather data from a list of european cities. Once data has been gathered it plots on a map

  python europeanTemperatureMap.py -o 1 -a xxxxxxxxxxxxx

  Usage: getCityWeather.py [options]

  Options:

                    -h, --help            show this help message and exit
                    -o OFFSET, --offset=OFFSET how fast in seconds weather has to be retrieved
                    -a API, --api=API     api key to get access to openweather

2. cities.csv: CSV file with the list of cities to retrieve weather data from

Example:

iata,airport,city,state,country,lat,long,temp
null,Madrid SP,Madrid,SP,SP,null,null,null
null,London Uk,London,UK,UK,null,null,null

Some of the columns are not used but they could be used in future script versions

Prerequisites

  Python Libraries


  Use library pyown to get weather data from http://openweathermap.org/. To install execute command

      pip install pyowm

  Use library plotly to plot a map with weather data https://plot.ly/

      pip install plotly

  Use library geopy to get cities coordinates https://github.com/geopy/geopy

      pip install geopy

  Extensions

  More weather data could be included in the map. Different kinds of maps and formats could be used.  In combination with nosql databases, weather data could be stored and analyzed to be displayed in the map.  
