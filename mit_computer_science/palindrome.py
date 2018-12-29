def is_palindrome(text):
    """检测回文字符串"""
    if len(text) <= 1:
        return True
    else:
        return text[0] == text[-1] and is_palindrome(text[1:-1])


def is_palindrome1(text, indent):
    """查看调用方式"""
    print(indent, text)
    if len(text) <= 1:
        print(indent)
        return True
    else:
        answer = text[0] == text[-1] and is_palindrome1(text[1:-1], indent + indent)
        print(indent, answer)
        return answer


is_palindrome1('abcba', '*')
