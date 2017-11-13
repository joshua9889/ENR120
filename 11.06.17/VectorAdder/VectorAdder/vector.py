# Lib for vector
import math

# Add two vectors together
def addVector(V1, V2):
    result_x = float(V1[0] + V2[0])
    result_y = float(V1[1] + V2[1])

    resultant_mag = ((result_x**2) + (result_y**2))**0.5
    resultant_ang = math.atan((result_y)/(result_x))

    return resultant_mag, resultant_ang


# Calculate a vector
def Vector(mag, rad):
    x = mag * math.cos(rad)
    y = mag * math.sin(rad)
    return x, y


# Convert radians to degrees
def rad2deg(rad):
    deg = float(rad)*180/math.pi
    return deg


# Convert degrees to radians
def deg2rad(deg):
    rad = float(deg)/180 * math.pi
    return rad


# Get the X component of a vector
def X_component(mag, rad):
    return Vector(mag, rad)[0]


# Get the Y component of a vectors
def Y_component(mag, rad):
    return Vector(mag, rad)[1]
