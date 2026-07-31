from calculator import add, subtract, multiply, divide

print("Python Calculator")
print("-----------------")

a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("\nChoose an operation")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = input("Enter your choice (1-4): ")

if choice == "1":
    print("Result =", add(a, b))

elif choice == "2":
    print("Result =", subtract(a, b))

elif choice == "3":
    print("Result =", multiply(a, b))

elif choice == "4":
    print("Result =", divide(a, b))

else:
    print("Invalid Choice")
