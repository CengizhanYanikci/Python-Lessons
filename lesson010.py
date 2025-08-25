import math


x=math.pi
print("-------------------Calculator (Circle Area)-------------------")

radiusCircle=float(input("Radius : "))    #radius


print("Area",x*(radiusCircle**2))


          
#         ***********     
#      *****       *****  
#     ***             *** 
#    ***               ***
#    **           5cm   **
#    **         --------**     ====> Area is "78.53981633974483"
#    **                 **
#    ***               ***
#     ***             *** 
#      *****       *****  
#         ***********     


print("-------------------Calculator (Plus)-------------------")


num1=float(input("Number 1 : "))
num2=float(input("Number 2 :"))
sum=num1 + num2

print("Result: ", sum)



print("----------------------------+ - / * -----------------")


# Ask the user to choose an operation
operation = str(input("Choose an operation: * / + - : "))

# Get the first number from the user
number1 = float(input("Number 1: "))

# Get the second number from the user
number2 = float(input("Number 2: "))

# Perform calculations
sum_result = number1 + number2        # Addition
difference = number1 - number2        # Subtraction
product = number1 * number2           # Multiplication
quotient = number1 / number2          # Division

# Check which operation the user selected and print the result
if operation == '+':
    print("Result:", sum_result)
elif operation == '-':
    print("Result:", difference)
elif operation == '*':
    print("Result:", product)
elif operation == '/':
    print("Result:", quotient)


