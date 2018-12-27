def duplicate_encode(word):
    new_word = ""
    for v in word:
        if word.count(v) > 1:
            new_word += ')'
        else:
            new_word += '('
    return new_word


print(duplicate_encode('justdoit'))
