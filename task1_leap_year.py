def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    return year % 4 == 0


def read_year():
    while True:
        text = input("Введіть рік: ")
        try:
            year = int(text)
        except ValueError:
            print("Рік має бути цілим числом.")
            continue
        if year < 1:
            print("Рік має бути додатним числом.")
            continue
        return year


def main():
    year = read_year()
    if is_leap(year):
        print(f"{year} - високосний рік")
    else:
        print(f"{year} - не високосний рік")


if __name__ == "__main__":
    main()
