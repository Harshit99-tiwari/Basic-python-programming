import math

def calculator():
    print("\n====== ADVANCED CALCULATOR ======")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("7. Square Root")
    print("8. Sin")
    print("9. Cos")
    print("10. Tan")
    print("0. Exit")

while True:
    calculator()
    choice = input("Enter your choice: ")

    if choice == "0":
        print("Calculator Closed ")
        break

    try:
        if choice in ["1", "2", "3", "4", "5", "6"]:
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))

            if choice == "1":
                print("Result:", a + b)
            elif choice == "2":
                print("Result:", a - b)
            elif choice == "3":
                print("Result:", a * b)
            elif choice == "4":
                if b == 0:
                    print("Error: Division by zero ")
                else:
                    print("Result:", a / b)
            elif choice == "5":
                print("Result:", a ** b)
            elif choice == "6":
                print("Result:", a % b)

        elif choice == "7":
            num = float(input("Enter number: "))
            print("Result:", math.sqrt(num))

        elif choice in ["8", "9", "10"]:
            angle = float(input("Enter angle in degrees: "))
            rad = math.radians(angle)

            if choice == "8":
                print("Result:", math.sin(rad))
            elif choice == "9":
                print("Result:", math.cos(rad))
            elif choice == "10":
                print("Result:", math.tan(rad))

        else:
            print("Invalid choice ")

    except ValueError:
        print("Error: Please enter valid numbers ")
