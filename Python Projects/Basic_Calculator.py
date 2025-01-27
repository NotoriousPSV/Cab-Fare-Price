#define the functions needed of add, subt, mult, and div
#print the options to the user
#Ask for values
#call the functions
#add a while loop to continue the program until the user wants to exit

def add(a, b):
    answer = a + b
    #Concatinating the strings
    print(str(a) + " + " + str(b) + " = " + str(answer))

def subt(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer))

def mult(a, b):
    answer = a * b
    print(str(a) + " * " + str(b) + " = " + str(answer))

def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer))

while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")

    choice = input("Your choice(Letter): ")

    if choice == "a" or choice == "A":
        print("Addition")
        #Use of int function is to convert our input to an integer
        a = int(input("First number: "))
        b = int(input("Second number: "))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("First number: "))
        b = int(input("Second number: "))
        subt(a, b)
    elif choice == "c" or choice == "C":
        print("Multiplication")
        a = int(input("First number: "))
        b = int(input("Second number: "))
        mult(a, b)
    elif choice == "d" or choice == "D":
        print("Division")
        a = int(input("First number: "))
        b = int(input("Second number: "))
        div(a, b)
    elif choice == "e" or choice == "E":
        print("Exit")
        quit()
    elif choice == "f65hd3dss7f0ro4j31vs3":
        print("You unlock the secret level! Thnak you for playing the calculator game!")
    else:
        print("Invalid option use error code: f65hd3dss7f0ro4j31vs3 to fix the error")