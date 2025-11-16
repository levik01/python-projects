print("Pattern Generator")
print("1. Right Triangle")
print("2. Square Pattern")
print("3. Number Pyramid")

choice = input("Choose pattern number: ")

n = int(input("Enter size: "))

if choice == "1":
    for i in range(1, n+1):
        print("*" * i)

elif choice == "2":
    for i in range(n):
        print("*" * n)

elif choice == "3":
    for i in range(1, n+1):
        for j in range(1, i+1):
            print(j, end=" ")
        print()

else:
    print("Invalid choice")