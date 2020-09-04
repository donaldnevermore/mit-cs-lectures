def is_palindrome(text):
    if len(text) <= 1:
        return True
    else:
        return text[0] == text[-1] and is_palindrome(text[1:-1])


def view_calls(text, indent):
    print(indent, text)
    if len(text) <= 1:
        print(indent)
        return True
    else:
        answer = text[0] == text[-1] and view_calls(text[1:-1], indent + indent)
        print(indent, answer)
        return answer


view_calls("abcba", '*')
