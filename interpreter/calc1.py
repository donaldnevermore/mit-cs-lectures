from typing import Optional
# Token types
#
# EOF (end-of-file) token is used to indicate that
# there is no more input left for lexical analysis
INTEGER, PLUS, MINUS, MUL, DIV, EOF = 'INTEGER', 'PLUS', 'MINUS', 'MULTI', 'DIV', 'EOF'


class Token:
    def __init__(self, type, value):
        # token type: INTEGER, PLUS, MINUS or EOF
        self.type = type
        # token value: 正整数, '-', '+', or None
        self.value = value

    def __str__(self):
        """字符串表示

        Examples:
            Token(INTEGER, 3)
            Token(PLUS, '+')
        """
        return f'Token({self.type}, {repr(self.value)})'

    def __repr__(self):
        return self.__str__()


class Interpreter:
    text: str
    pos: int
    current_token: Optional[Token]
    current_char: Optional[str]

    def __init__(self, text):
        # 输入的字符串
        self.text = text
        # 字符串索引
        self.pos = 0
        # 当前字符
        self.current_token = None
        self.current_char = self.text[self.pos]

    def error(self):
        raise Exception('无效的语法')

    def advance(self):
        """移动 pos 指针， 设置好 current_char"""
        self.pos += 1
        if self.pos > len(self.text) - 1:
            # 到达最后一个字符了
            self.current_char = None
        else:
            self.current_char = self.text[self.pos]

    def skip_whitespace(self):
        while self.current_char is not None and self.current_char.isspace():
            self.advance()

    def integer(self):
        result = ''
        while self.current_char is not None and self.current_char.isdigit():
            result += self.current_char
            self.advance()
        return int(result)

    def get_next_token(self):
        """词法分析器，生成 Token"""
        while self.current_char is not None:
            if self.current_char.isspace():
                self.skip_whitespace()
                continue

            if self.current_char.isdigit():
                return Token(INTEGER, self.integer())

            if self.current_char == '+':
                self.advance()
                return Token(PLUS, '+')

            if self.current_char == '-':
                self.advance()
                return Token(MINUS, '-')

            if self.current_char == '*':
                self.advance()
                return Token(MUL, '*')

            if self.current_char == '/':
                self.advance()
                return Token(DIV, '/')

            self.error()

        return Token(EOF, None)

    def eat(self, token_type):
        """
        compare the current token type with the passed token
        type and if they match then "eat" the current token
        and assign the next token to the self.current_token,
        otherwise raise an exception.
        :param token_type:
        :return:
        """
        if self.current_token.type == token_type:
            self.current_token = self.get_next_token()
        else:
            self.error()

    def term(self):
        """取一个整数 Token 并返回值"""
        token = self.current_token
        self.eat(INTEGER)
        return token.value

    def expr(self):
        """解析器/解释器

        expr -> INTEGER PLUS INTEGER
        expr -> INTEGER MINUS INTEGER
        """
        # 设置第一个 Token
        self.current_token = self.get_next_token()

        result = self.term()

        while self.current_token.type in (PLUS, MINUS, MUL, DIV):
            token = self.current_token

            if token.type == PLUS:
                self.eat(PLUS)
                result = result + self.term()
            elif token.type == MINUS:
                self.eat(MINUS)
                result = result - self.term()
            elif token.type == MUL:
                self.eat(MUL)
                result = result * self.term()
            elif token.type == DIV:
                self.eat(DIV)
                result = result // self.term()

        return result


def main():
    while True:
        try:
            text = input('calc> ')
        except EOFError:
            break

        if not text:
            continue

        interpreter = Interpreter(text)
        result = interpreter.expr()
        print(result)


if __name__ == '__main__':
    main()
