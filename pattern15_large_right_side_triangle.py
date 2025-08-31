rows = 5
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()

rows = 4
for i in range(rows, 0, -1):
    for j in range(1, i + 1):
        print("*", end="")
    print()