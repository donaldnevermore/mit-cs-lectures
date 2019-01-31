INTEGER, PLUS, MUL, EOF = 'INTEGER', 'PLUS', 'MUL', 'EOF'


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value


class Lexer:
    text: str
    current_token: Token
    pos: int = 0

    def __init__(self, text):
        self.text = text

    def get_next_token(self):
        if self.pos > len(self.text) - 1:
            self.current_token = Token(EOF, None)
            return self.current_token

        current_text = self.text[self.pos]
        self.pos += 1
        if current_text.isdigit():
            self.current_token = Token(INTEGER, int(current_text))
        elif current_text == '+':
            self.current_token = Token(PLUS, '+')
        elif current_text == '*':
            self.current_token = Token(MUL, '*')

        return self.current_token

    def term(self):
        result = self.factor().value

        if self.get_next_token().type == MUL:
            result *= self.factor().value

        return result

    def factor(self):
        return self.get_next_token()


class Interpreter:
    def __init__(self, lexer):
        self.lexer = lexer

    def expr(self):
        result = self.lexer.get_next_token().value

        if self.lexer.get_next_token().type == PLUS:
            result += self.lexer.term()

        print(result)


lexer = Lexer('2+7*3')
interpreter = Interpreter(lexer)
interpreter.expr()
