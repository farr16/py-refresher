print("Welcome to the n-queens problem solver")
size = 0
while True:
    try:
        size = int(input("Enter the size of board to solve for: "))
    except ValueError:
        print("Error: Input must be a positive integer. Try again.")
    else:
        break

print("Size of board: ", size)
