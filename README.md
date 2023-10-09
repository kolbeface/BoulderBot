# BoulderBot
This program checks for rain at a certain lat/long and starts a timer for 48 hours and notifies when climbing is allowed again.

weather.py is where I make an api call to look at current weather conditions for the specified lat/long (currently set to sandston) using https://openweathermap.org/ api
timer.py defines to function for a constant weather monitoring function as well as a climbing lockout period after rain
BoulderBot.py uses the afformentioned files in order to produce guidance on weather or not it is a good idea to climb at the specified location.