#Program to find area of the circle

Pi = 3.14
r= float(input ("Enter the radius of the circle"))
area = float(Pi * r * r)
print("Area of the circle is :", area)

#   OR
import math
radius = float(input("Enter the Radius of the circle"))
print(math.pi)
area = math.pi*pow(radius,2)
print(area)



#Take two inputs from user and print which is greater , lesser , equal to

num_1 = input("Enter the first number")
num_2 = input("Enter the second number")
print("First number is greater than second number", num_1>num_2)
print(num_1 < num_2)
print(num_1 >= num_2)


#To find the sqrt root & Cube root of the number

import math
result = math.sqrt(2)
print(result)

#Cube root

import math
number = float(input("Enter the number"))
#cube = number**3
cube = math.pow(number,3)
print(cube)




