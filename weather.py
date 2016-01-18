#!/usr/bin/python

######################################################################
# Author: Aarsh Patil                                                #
# Version: 0.1 alpha                                                 #
# Program: Displays current weather according to the city            #
######################################################################

import os,sys
import pyowm

#print sys.argv[1]
owm = pyowm.OWM('2c7cb540acc670c661d2758545a0d56a')

currentWeather = owm.weather_at_place('London')
placeWeather = currentWeather.get_weather()
print placeWeather.get_wind()
print placeWeather.get_temperature('celsius')




