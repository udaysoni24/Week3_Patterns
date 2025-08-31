n = 6
for i in range(1, n + 1):
    for j in range(1, 3):  # Only two columns: left and diagonal
        if j == 1 or j == n - i + 1:
            print("*", end="")
        else:
            print("_", end="")
    print()