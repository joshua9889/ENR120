# Custom Lib I made for vectors
from vector import *

# Get values from an input in the format "1200, deg(30)" or 1200, rad(0.523598775598)
def getValuesFromString(String):
    mag = True  # Used to find the magitude from input
    magString = ''
    degString = ''
    measureStartPos = 0  # Used to find the measurment type of the angle
    measureEndPos = 0

    # Remove all spaces
    String = String.replace(" ", '')

    # Interate over all values inputed and split them up
    for i in range(len(String)):
        if String[i] == ',':
            mag = False
            measureStartPos = i+1
            measureEndPos = measureStartPos + 3
        else:
            if mag:
                magString += str(String[i])
            else:
                degString += String[i]

    # Determine what the measurement
    if degString[0:3] == 'deg':
        degString = degString.replace("deg", "")
        deg = True
    else:
        degString = degString.replace("rad", "")
        deg = False

    # Remove the parentheses
    degString = degString.replace("(", "")
    degString = degString.replace(")", "")

    # Convert to a "real" number
    angle = eval(degString)
    magnitude = eval(magString)

    # Convert angle to radians
    if deg:
        angle = deg2rad(angle)

    return magnitude, angle

def main():
    # Ask the user to input the two vectors
    print "Enter a vector in the format '1200, deg(30)' or '1200, rad(3.145)'"
    V1String = str(raw_input("Please enter the first vector: "))
    V2String = str(raw_input("Please enter the second vector: "))

    # Data for the first vector
    V1Data = getValuesFromString(V1String)
    v1 = Vector(V1Data[0], V1Data[1])

    # Data for the second vector
    V2Data = getValuesFromString(V2String)
    v2 = Vector(V2Data[0], V2Data[1])

    # Add the vectors together
    resultant_vector = addVector(v1, v2)

    # Output to console
    print "Magnitude: " + str(resultant_vector[0])
    print "Angle (Deg): " + str(rad2deg(resultant_vector[1]))

if __name__ == '__main__':
    main()
