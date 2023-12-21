# Function to add two numbers
def add(num1, num2):
    return num1 + num2
 
# Function to subtract two numbers
def subtract(num1, num2):
    return num1 - num2
 
# Function to multiply two numbers
def multiply(num1, num2):
    return num1 * num2
 
# Function to divide two numbers
def divide(num1, num2):
    return num1 / num2
 
print("Please select operation -\n" \
        "1. Add\n" \
        "2. Subtract\n" \
        "3. Multiply\n" \
        "4. Divide\n")
 
while True:
    # Take input from the user
    option = input("Enter option (1/2/3/4): ")

    # check if choice is one of the four options
    if option in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
 
        if option == '1':
            print(num1, "+", num2, "=",
                            add(num1, num2))
        
        elif option == '2':
            print(num1, "-", num2, "=",
                            subtract(num1, num2))
        
        elif option == '3':
            print(num1, "*", num2, "=",
                            multiply(num1, num2))
        
        elif option == '4':
            print(num1, "/", num2, "=",
                            divide(num1, num2))
            
        # break the while loop if answer is no
        further_calculation = input("Let's do next calculation? (yes/no): ")
        if further_calculation == "no":
          break

    else:
            print("Invalid input")