PLUS = 'PLUS'
MINUS = 'MINUS'
INTEGER = 'INTEGER'


class Token:

    def __init__(self, type, value):
        self.type = type
        self.value = value


class Interpreter:
    text: str
    pos: int = 0
    current_token = None

    def __init__(self, text):
        self.text = text

    def get_next_token(self):
        if self.pos >= len(self.text):
            return None

        char = self.text[self.pos]

        if char == '+':
            self.current_token = Token(PLUS, '+')
        elif char == '-':
            self.current_token = Token(MINUS, '-')
        else:
            self.current_token = Token(INTEGER, int(char))

        self.pos += 1

        return self.current_token

    def expr(self):

        result: int = 0

        first = self.get_next_token()

        result = first.value

        token = self.get_next_token()
        while token is not None:
            if token.type == PLUS:
                token = self.get_next_token()
                result += token.value
            elif token.type == MINUS:
                token = self.get_next_token()
                result -= token.value
            else:
                token = self.get_next_token()
                continue

        print(result)


i = Interpreter('7-3+2-1')
i.expr()
