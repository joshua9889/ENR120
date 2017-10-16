# -*- coding: utf-8 -*-

# method to calculate windspeed
# T is the temperature in degrees Fahrenheit
# mph
def calculateWindChill(F, mph):
    if F <= 50 and mph > 3:
        wind_chill = 35.74 + .6215*F - 35.75*mph**0.16 + 0.4275*F*mph**0.16
    else:
        wind_chill = F
    return wind_chill

# Var defs
userDegF = 0 
userWindSpeedMph = 0

while True: # Get a valid input
    try:
        userDegF = input("Please enter the temperture in Fahrenheit: ")
        if userDegF > 50:
            print "Try entering a number less than or equal to 50."
        else:
            break
    except:
        print "Try using numbers"

while True: # Get a valid input
    try:
        userWindSpeedMph = input("Please enter a wind speed: ")
        if userWindSpeedMph < 3:
            print "Try entering a number greater than 3."
        else:
            break
    except:
        print "Try using numbers"

# Print Headers
print repr("Temperature").rjust(0),
print repr("Wind Speed").rjust(0),
print repr("Wind Chill").rjust(0)

for i in range(0, 20, 2):
    localWindSpeed = userWindSpeedMph+i # Get wind speed to calculate
    windChill = round(calculateWindChill(userDegF, localWindSpeed), 1) # Calculate wind chill to one degree

    # Print the values
    print repr(userDegF).rjust(7),
    print repr(localWindSpeed).rjust(13),
    print repr(windChill).rjust(13)

