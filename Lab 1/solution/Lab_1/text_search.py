import re
ls = ['she', 'sells', 'sea', 'shells', 'by', 'the', 'sea', 'shore']


def E1(ls):
    for word in ls:
        # \A denote start of string, and () is a capturing group containing the token "sh".
        if re.match(r'\A(sh)', word):
            print(word)


def E1_2(ls):
    for word in ls:
        # String splitting to only look at the first to char and check if they match
        if 'sh' in word[:2]:
            print(word)


def E2(ls):
    for word in ls:
        # Looking for any sequence of word_chars \w that is of the length (4 -> Infinity
        if re.match(r'[\w]{4,}', word):
            print(word)


def E2_2(ls):
    for word in ls:
        if len(word) > 4:
            print(word)


E2(ls)
