def read_height():
    while True:
        text = input("Введіть висоту трикутника: ")
        try:
            height = int(text)
        except ValueError:
            print("Висота має бути цілим числом.")
            continue
        if height < 1:
            print("Висота має бути додатним числом.")
            continue
        return height


def main():
    height = read_height()
    base_width = len(" ".join([str(height)] * height))
    for row in range(1, height + 1):
        line = " ".join([str(row)] * row)
        print(line.center(base_width).rstrip())


if __name__ == "__main__":
    main()
