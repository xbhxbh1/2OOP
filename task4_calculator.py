text = input("Введіть вираз: ")
tokens = text.split()

# Крок 1: спочатку виконуємо множення і ділення
i = 0
while i < len(tokens):
    if tokens[i] == "*" or tokens[i] == "/":
        left = float(tokens[i - 1])
        right = float(tokens[i + 1])
        if tokens[i] == "*":
            value = left * right
        else:
            value = left / right
        tokens[i - 1] = str(value)
        tokens.pop(i)
        tokens.pop(i)
    else:
        i = i + 1

# Крок 2: потім додавання і віднімання зліва направо
result = float(tokens[0])
i = 1
while i < len(tokens):
    if tokens[i] == "+":
        result = result + float(tokens[i + 1])
    else:
        result = result - float(tokens[i + 1])
    i = i + 2

if result == int(result):
    result = int(result)

print("Відповідь:", result)
