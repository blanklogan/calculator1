
while True:
    operation = input("Would you like to add, subtract, multiply, or divide? ")
    if operation == "add":
        number1_input = input("Enter your first number. ")
        number2_input = input("Enter your second number. ")
        number1 = int(number1_input)
        number2 = int(number2_input)
        result = number1 + number2
        print (f"Answer = {result}")  
        break
    if operation == "subtract":
        number1_input = input("Enter your first number. ")
        number2_input = input("Enter your second number. ")
        number1 = int(number1_input)
        number2 = int(number2_input)
        result = number1 - number2
        print (f"Answer = {result}")
        break
    if operation == "multiply":
        number1_input = input("Enter your first number. ")
        number2_input = input("Enter your second number. ")
        number1 = int(number1_input)
        number2 = int(number2_input)
        result = number1 * number2
        print (f"Answer = {result}")
        break
    if operation == "divide":
        number1_input = input("Enter your first number. ")
        number2_input = input("Enter your second number. ")
        number1 = int(number1_input)
        number2 = int(number2_input)
        result = number1 / number2
        print (f"Answer = {result}")
        break
    else:
        print("Try again") 
