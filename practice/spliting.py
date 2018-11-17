#This will split the words in the string
def split_word(words):
    word = words.split()
    return word
def sort(words):
    letters = sorted (words)
    return letters
def print_first_word(words):
    word = words.split()[0]
    print(word)
def print_last_word(words):
    word = words.split()[-1]
    print(word)
def sort_sentence(words):
    word = split_word(words)
    sort = sort(word)
    return word
def print_first_last_sorted_sentence(words):
    word = sorted(split_word(words))
    first = word.pop(0)
    last = word.pop(-1)
    print(first)
    print(last)