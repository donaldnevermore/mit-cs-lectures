import pytest
from calc import Lexer, Interpreter


def text_to_result(text):
    lexer = Lexer(text)
    interpreter = Interpreter(lexer)
    result = interpreter.expr()
    return result


def test_long_input():
    text1 = '7 + 3 * (10 / (12 / (3 + 1) - 1)) / (2 + 3) - 5 - 3 + (8)'
    result1 = text_to_result(text1)
    assert result1 == 10

    text2 = '7 + ((8 + 2)) * (4 - 2)'
    result2 = text_to_result(text2)
    assert result2 == 27
