a = 30
b = 20
c = 45
d = 15

result1 = (a>b)
result2 = (c>d)
result3 = result1 and result2
print(result3)

#Max of 3 numbers

num1 = int(input("Enter the number 1"))
num2 = int(input("Enter the number 2"))
num3 = int(input("Enter the number 3"))

Max_Number = max((num1, num2, num3))
print("Maximum number is ", Max_Number)

#By using if

num1 = int(input("Enter the number 1"))
num2 = int(input("Enter the number 2"))
num3 = int(input("Enter the number 3"))
if num1 > num2 and num1 > num3:
     print("max is", num1)
elif num2 > num1 and num2 > num3:
    print("Max is",num2)
else:
    print("Max is num3",num3)




