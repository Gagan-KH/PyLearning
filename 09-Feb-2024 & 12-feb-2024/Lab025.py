#factorial of Number

# num = int(input("Enter a number: "))
#
# if num < 0:
#     print("Factorial is not defined for negative numbers.")
# else:
#     factorial = 1
#     for i in range(1, num + 1):
#         factorial = factorial*i
# print(f"The factorial of {num} is: {factorial}")


#Fibonacci

a, b =0, 1
while a < 10:
    print(a, end=" ")
    a, b = b, a + b
