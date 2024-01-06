# programming logic :
# 1) accept input
# 2) define operation such as:
# addition
# subtraction
# multiplication
# division 
# 3)implement operation 
# 4) display output

a = int(input("a = "))
b = int(input("b = "))

def Addition():
    c = a + b
    print(c)

def Subtraction():
    c = a - b
    print(c)

def Multiplication():
    c = a * b
    print(c)

def Division():
    c = a / b
    print(c)

while True:
    print("\n")
    print("Welcome to Calculator project")
    print("Please select the arithmetic operation you would like to perform:")
    print("1.Addition")
    print("2.Subtraction")
    print("3.Multiplication")
    print("4.Division")

    operation = int(input("Please Enter your choice:"))

    if operation == 1:
        Addition()
    elif operation == 2:
        Subtraction()
    elif operation == 3:
        Multiplication()
    elif operation == 4:
        Division()
    else:
        print("Invalid Input!!")
        break
