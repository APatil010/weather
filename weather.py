#!/usr/bin/python

######################################################################
# Author: Aarsh Patil                                                #
# Version: 0.2 alpha                                                 #
# Program: Displays current weather according to the city            #
######################################################################

import os,sys
import pyowm

#declaration for variables
degree_sign= u'\N{DEGREE SIGN}'

#API key for the OWM
owm = pyowm.OWM('2c7cb540acc670c661d2758545a0d56a')

#pass the location parameter to the API
currentWeather = owm.weather_at_place('London')
placeWeather = currentWeather.get_weather()

#get inputs from API
wind = placeWeather.get_wind()
temperature = placeWeather.get_temperature('celsius')
humidity = placeWeather.get_humidity()

print "******************************"
print "* "
print "* Temperature : "
print "*             Current  : ",temperature['temp'],degree_sign,"C"
print "*             Max      : ",temperature['temp_max'],degree_sign,"C"
print "*             Min      : ",temperature['temp_min'],degree_sign,"C"
print "* "
print "* "
print "* Humidity    : ",humidity," %"
print "* "
print "* "
print "* Wind        : "
print "*             Speed  : ",wind['speed'],"m/s"
print "*             Degree : ",wind['deg'],degree_sign
print "* "
print "******************************"

