"""
Write a function that accepts string from user, return a sentence with the words reversed. We are ready -> ready are We
"""


def To_reverse(str):
    words = str.split()
    words = list(reversed(words))
    return " ".join(words)


string = input()

print(To_reverse(string))
