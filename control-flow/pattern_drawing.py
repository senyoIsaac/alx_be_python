size = int(input("Enter the size of the pattern: "))

# Initialize row counter
row = 0

# Outer while loop for rows
while row < size:
    # Inner for loop for columns
    col = 0
    while col < size:
        print("*", end="")
        col += 1
    # New line after each row
    print()
    row += 1