# Function for addition
def add(a, b):
    return a + b

# Function for subtraction
def subtract(a, b):
    return a - b

# Function for multiplication
def multiply(a, b):
    return a * b

# Function for division
def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed!"

# Main program
print("Welcome to the best calculator ever created!!")  # This line print the greetings message
num1 = float(input("Enter the first number: "))  # This two lines required 2 
num2 = float(input("Enter the second number: ")) # numbers to the user 

print("\nResults:")
print(f"Addition: {add(num1, num2)}")               # these lines print each result
print(f"Subtraction: {subtract(num1, num2)}")       # of the functions created before
print(f"Multiplication: {multiply(num1, num2)}")
print(f"Division: {divide(num1, num2)}")
