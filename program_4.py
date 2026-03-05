import math

distance1 = []
distance2 = []

def distance(coord1, coord2):
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2

    dist = math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)
    return dist

def main():
    try:
        print("First 3D coordinates")
        x1 = int(input("Enter first 'x' coordinate: "))
        y1 = int(input("Enter first 'y'  coordinate: "))
        z1 = int(input("Enter first 'z' coordinate: "))

        print("Second 3D coordinates")
        x2 = int(input("Enter second 'x' coordinate: "))
        y2 = int(input("Enter second 'y' coordinate: "))
        z2 = int(input("Enter second 'z' coordinate: "))

        coord1 = [x1, y1, z1]
        coord2 = [x2, y2, z2]

        result = distance(coord1, coord2)

        print(f"The distance between these coordinates is: {result:.2f}")

    except ValueError:
        print("Error. Please enter a valid coordinate.")

main()