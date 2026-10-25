import re

TOKEN_RE = re.compile(r"[0-9]+(?:\.[0-9]+)?|[-+*/()]")


def tokenize(text):
    tokens = []
    position = 0
    while position < len(text):
        if text[position].isspace():
            position += 1
            continue
        match = TOKEN_RE.match(text, position)
        if match is None:
            raise ValueError(f"невідомий символ '{text[position]}'")
        tokens.append(match.group())
        position = match.end()
    return tokens


class Parser:
    """Обчислює вираз з урахуванням пріоритету: * і / виконуються раніше за + і -."""

    def __init__(self, tokens):
        self.tokens = tokens
        self.position = 0

    def peek(self):
        if self.position < len(self.tokens):
            return self.tokens[self.position]
        return None

    def take(self):
        token = self.peek()
        self.position += 1
        return token

    def parse(self):
        if not self.tokens:
            raise ValueError("вираз порожній")
        value = self.expression()
        if self.peek() is not None:
            raise ValueError(f"неочікуваний символ '{self.peek()}'")
        return value

    def expression(self):
        value = self.term()
        while self.peek() in ("+", "-"):
            if self.take() == "+":
                value += self.term()
            else:
                value -= self.term()
        return value

    def term(self):
        value = self.factor()
        while self.peek() in ("*", "/"):
            if self.take() == "*":
                value *= self.factor()
            else:
                divisor = self.factor()
                if divisor == 0:
                    raise ZeroDivisionError
                value /= divisor
        return value

    def factor(self):
        token = self.take()
        if token is None:
            raise ValueError("вираз незавершений")
        if token == "-":
            return -self.factor()
        if token == "+":
            return self.factor()
        if token == "(":
            value = self.expression()
            if self.take() != ")":
                raise ValueError("немає закриваючої дужки")
            return value
        if token[0].isdigit():
            return float(token)
        raise ValueError(f"неочікуваний символ '{token}'")


def format_number(value):
    value = round(value, 10)
    if value.is_integer():
        return str(int(value))
    return str(value)


def main():
    text = input("Введіть вираз: ")
    try:
        result = Parser(tokenize(text)).parse()
    except ZeroDivisionError:
        print("Помилка: ділення на нуль")
        return
    except ValueError as error:
        print(f"Помилка: {error}")
        return
    print(f"Відповідь: {format_number(result)}")


if __name__ == "__main__":
    main()
