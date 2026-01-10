#Smart password strength Analyzer and generator
import random
import string

def check_strength(password):
    score = 0
    remarks = []

    if len(password) >= 8:
        score += 1
    else:
        remarks.append("Password too short (min 8 characters)")

    if any(char.isupper() for char in password):
        score += 1
    else:
        remarks.append("Add at least one uppercase letter")

    if any(char.islower() for char in password):
        score += 1
    else:
        remarks.append("Add at least one lowercase letter")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        remarks.append("Add at least one digit")

    if any(char in string.punctuation for char in password):
        score += 1
    else:
        remarks.append("Add at least one special character")

    return score, remarks


def generate_password():
    length = 12
    chars = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(chars) for _ in range(length))


while True:
    print("\n====== SMART PASSWORD TOOL ======")
    print("1. Check Password Strength")
    print("2. Generate Strong Password")
    print("0. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        pwd = input("Enter password: ")
        score, remarks = check_strength(pwd)

        print("\nStrength Score:", score, "/ 5")

        if score == 5:
            print(" Strong Password")
        elif score >= 3:
            print("⚠ Medium Password")
        else:
            print(" Weak Password")

        if remarks:
            print("\nImprovements needed:")
            for r in remarks:
                print("-", r)

    elif choice == "2":
        print(" Generated Strong Password:", generate_password())

    elif choice == "0":
        print("Exiting... Stay Secure 🔒")
        break

    else:
        print("Invalid choice ")
