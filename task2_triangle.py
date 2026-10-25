height = int(input("Введіть висоту трикутника: "))

for row in range(1, height + 1):
    spaces = " " * (height - row)
    numbers = (str(row) + " ") * row
    print(spaces + numbers)
