# OK
def duplicate_encode(word):
    newWord = ""
    for v in word:
        if word.count(v) > 1:
            newWord += ')'
        else:
            newWord += '('
    return newWord


print(duplicate_encode('justdoit'))
