from pythainlp.transliterate import romanize
from pythainlp.tokenize import word_tokenize

def trans_thai(input):
    inputStr = input.strip()
    inputNoSpaces = inputStr.replace(' ', '')
    wordz = word_tokenize(inputNoSpaces, engine="newmm")
    word_list = []
    for word in wordz:
        if word == ' ':
            word_list.append('.')
            continue
        if word == '/':
            word_list.append('/')
            continue
        if word == '.':
            word_list.append('.')
            continue
        if word == ',':
            word_list.append(',')
            continue
        if word == '(':
            word_list.append('(')
            continue
        if word == ')':
            word_list.append(')')
            continue
        if word == '+':
            word_list.append('+')
            continue
        if word == '-':
            word_list.append('-')
            continue
        if word.isnumeric() or is_number(word):
            word_list.append(word)
            continue

        rom_word = romanize(word, engine="thai2rom")
        word_list.append(rom_word)

    separator = " "

    return separator.join(word_list)

def is_number(numString):
    if numString.isnumeric():
        return True
    if numString.isalpha():
        return False
    if '.' in numString:
        parts = numString.split('.')
        for part in parts:
            wholeIsNumeric = False
            if part.isalpha() or part.isalnum() == False:
                wholeIsNumeric = False
                break
            elif part.isnumeric():
                wholeIsNumeric = True
        return wholeIsNumeric
    return False