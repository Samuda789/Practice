# I created 4 functions for addition, multiplication, substraction and division
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


# Displaying the 4 operations
print("Select operation.\n1.Add(+)\n2.Subtract(-)\n3.Multiply(x)\n4.Divide(/)")

# I created a while loop in order to run the program for multiple times
while True:
    choice = input("Choose your operator(1,2,3,4): ")

    if choice in ("1", "2", "3", "4"):
        # the try function let's me check for errors in this block of code
        # the except function let's me handle the error
        # the ValueError will be raised if the user inputs a non-int value in num_1 and num_2
        try:
            num_1 = int(input("Enter first number: "))
            num_2 = int(input("Enter second number: "))
        except ValueError:
            print("Invalid input. please enter a number.")
            continue

        if choice == "1":
            print(num_1, "+", num_2, "=", add(num_1, num_2))
        elif choice == "2":
            print(num_1, "-", num_2, "=", subtract(num_1, num_2))
        elif choice == "3":
            print(num_1, "*", num_2, "=", multiply(num_1, num_2))
        elif choice == "4":
            print(num_1, "/", num_2, "=", divide(num_1, num_2))

        # created a new variable that decides whether to continue the programm or stop
        next_calculation = input("Would you like to do another calculation(yes/no): ")
        if next_calculation == "no":
            break
    else:
        print("Invalid input")
