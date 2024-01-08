while True:
    number1 = int(input("enter a integer: "))
    number2 = int(input("enter a integer: "))

    
    operator = str(input("choose your operator(+,-,x or /): "))

    if operator == "+" or "-" or "x" or "/":
        print("hooyda was!!!")

    if operator == "+":
        print(number1 + number2)
    elif operator == "-":
        print(number1 - number2)
    elif operator == "x":
        print(number1 * number2)    
    elif operator == "/":
        print(number1 // number2)

