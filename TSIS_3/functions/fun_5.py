"""
Write a function that accepts string from user and print all permutations of that string
"""


def permute(str, answer=""):
    if len(str) == 0:
        print(answer, end="\n")
        return

    for i in range(len(str)):
        ch = str[i]
        left_substr = str[0:i]
        right_substr = str[i + 1:]
        rest = left_substr + right_substr
        permute(rest, answer + ch)


s = "ABCDE"

permute(s)
