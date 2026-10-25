POINTS_PER_ANSWER = 100

# (питання, варіанти відповідей, номер правильної відповіді)
QUESTIONS = [
    (
        "Які кольори має прапор України?",
        ["жовтий і блакитний", "червоний і зелений", "чорний і жовтий", "зелений і фіолетовий"],
        1,
    ),
    (
        "У якому місті знаходиться ДТЕУ?",
        ["Вінниця", "Київ", "Львів", "Одеса"],
        2,
    ),
    (
        "Скільки планет у Сонячній системі?",
        ["7", "8", "9", "10"],
        2,
    ),
    (
        "Яка річка є найдовшою в Україні?",
        ["Дністер", "Південний Буг", "Дніпро", "Сіверський Донець"],
        3,
    ),
    (
        "Хто написав збірку віршів «Кобзар»?",
        ["Іван Франко", "Леся Українка", "Григорій Сковорода", "Тарас Шевченко"],
        4,
    ),
]


def read_choice(options_count):
    while True:
        text = input("Ваша відповідь (номер): ")
        try:
            choice = int(text)
        except ValueError:
            choice = 0
        if 1 <= choice <= options_count:
            return choice
        print(f"Введіть число від 1 до {options_count}.")


def main():
    score = 0
    for number, (question, options, correct) in enumerate(QUESTIONS, start=1):
        print(f"Current User Score: {score}")
        print(f"Питання {number}, {question}")
        print()
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option}")
        print()

        if read_choice(len(options)) != correct:
            print("Wrong Answer")
            print(f"Кінець програми. Ваш рахунок: {score}")
            return

        print("Correct answer")
        score += POINTS_PER_ANSWER

    print(f"Current User Score: {score}")
    print("Вітаємо! Ви відповіли на всі питання. Кінець програми.")


if __name__ == "__main__":
    main()
