def count_words(book):
    num_of_words = 0
    words = book.split()
    for word in words:
        num_of_words += 1
    return num_of_words

def character_count(book):
    word_dictionary = {}
    book = book.lower()
    for char in book:
        if (char in word_dictionary):
            word_dictionary[char] += 1
        else:
            word_dictionary[char] = 1
    return word_dictionary

def sort_on(d):
    return d["num"]

def sorted_dictionaries(word_dictionary):
    dictionary_list = []
    for ch in word_dictionary:
        dictionary_list.append({"char": ch, "num": word_dictionary[ch]})
    dictionary_list.sort(reverse=True, key=sort_on)
    return dictionary_list
    