"""
simple python calculator program 
performs arithmetic operators: addition, substraction, multiplication, division
prompts the user for input and loops until the user decided to stop. 
"""

def add(x, y):      #module for addition
    return x + y

def sub(x, y):      #module for subtraction
    return x - y

def mult(x, y):     #module for multiplication
    return x * y

def div(x, y):      #module for division
    if y == 0:
        return "Cannot divide by zero"
    return x / y

def cal():
    while True:
        try:                                        #perform these tasks, if nothing goes wrong 
            x = float(input("Enter first number: "))
            arth_ope = input("Enter operator (+, -, *, /): ")
            y = float(input("Enter second number: "))

            if arth_ope == '+':                     #call relative modules for user input
                print("Result: " + str(add(x, y)))
            elif arth_ope == '-':
                print("Result: " + str(sub(x, y)))
            elif arth_ope == '*':
                print("Result: " + str(mult(x, y)))
            elif arth_ope == '/':
                print("Result: " + str(div(x, y)))
            else:
                print("⚠️ Invalid operator. Please use +, -, *, or /")

        except ValueError:                          #if the input is not relevant, prompt error; preventing the program from crashing              
            print("⚠️ Please enter valid numbers.")

        again = input("Do you want to calculate again? (y/n): ").lower()  #ask the user to loop or break
        if again != 'y':
            print("Thank you for using the calculator!")
            break

cal()


