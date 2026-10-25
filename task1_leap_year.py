year = int(input("Введіть рік: "))

if year % 400 == 0:
    print(year, "- високосний рік")
elif year % 100 == 0:
    print(year, "- не високосний рік")
elif year % 4 == 0:
    print(year, "- високосний рік")
else:
    print(year, "- не високосний рік")
