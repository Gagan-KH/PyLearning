#Program to print the name of the triangle

side1 = float(input("Enter the side one"))
side2 = float(input("Enter the side Two"))
side3 = float(input("Enter the side Three"))

if side1 == side2 == side3:
    print("EQ")
elif side1 == side2 or side1 == side3 or side2 == side3:
    print("iso")
else:
    print("Scalene")