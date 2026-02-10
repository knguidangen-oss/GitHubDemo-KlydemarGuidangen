print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

pick = int(input("Enter your choice: "))
x = int(input("Enter number 1: "))
y = int(input("Enter number 2: "))

if pick == 1:
    print(x + y)
elif pick == 2:
    print(x - y)
elif pick == 3:
    print(x * y)
elif pick == 4:
    if y != 0:
        print(x / y)
    else:
        print("Error: Cannot divide by zero")
else:
    print("Invalid choice")
