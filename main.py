import math
# Function for addition
def addition(a, b):
    return a + b

# Function for subtraction
def subtraction(a, b):
    return a - b

# Function for multiplication
def multiplication(a, b):
    return a * b

# Function for division
def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed!"
def expo (a,b):
    return math.pow(a,b)
    

# Main program
print("Basic Arithmetic Operations")  # This line print the greetings message
num1 = float(input("Enter the first number: "))  # This two lines required 2 
num2 = float(input("Enter the second number: ")) # numbers to the user 

print("\nResults:")
print(f"Addition: {addition(num1, num2)}")               # these lines print each result
print(f"Subtraction: {subtraction(num1, num2)}")       # of the functions created before
print(f"Multiplication: {multiplication(num1, num2)}")
print(f"Division: {division(num1, num2)}")
print(f"Exponential: {expo(num1, num2)}")

